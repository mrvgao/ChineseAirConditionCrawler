import csv
import os


class SavedCities:
    def __init__(self):
        self.saved_file = 'saved'
        self.saved_filenames = []
        self.__load_saved_cities()

    def save_cities_info(self, city, y, m):
        info = [city, y, m]
        if info not in self.saved_filenames:
            with open(self.saved_file, 'a') as f:
                writer = csv.writer(f)
                writer.writerows([info])
            self.saved_filenames.append(info)

    def __load_saved_cities(self):
        if not os.path.exists(self.saved_file):
            return

        with open(self.saved_file, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                self.saved_filenames.append(row)

        return self.saved_filenames

    def already_saved(self, city, y, m):
        return [city, y, m] in self.saved_filenames

if __name__ == '__main__':
    saved_city_manager = SavedCities()
    saved_city_manager.save_cities_info('hangzhou', 2015, 10)
    assert saved_city_manager.already_saved('hangzhou', 2015, 10) == True
    assert saved_city_manager.already_saved('hangzhou', 2015, 9) == False
    print('test done!')