__author__ = 'Minchiuan Gao'
__mail__ = 'minchiuan.gao@gmail.com'

'''
Get Location Map information, such as map 杭州 => hangzhou
'''

import requests
from bs4 import BeautifulSoup


def get_location_html():
    http_url = 'http://www.tianqihoubao.com/aqi/'
    r = requests.get(http_url)
    r.encoding = 'GBK'
    html_file = r.text
    return html_file


def parse_location(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    CITY_CHECK = '.citychk > dl > dd > a'

    city_map = []

    city_check = soup.select(CITY_CHECK)

    for c in city_check:
        coding = c['href'].split('/')[2].replace('.html', '')
        city = c.string
        city_map.append((city, coding))

    return city_map


def save_city_map(city_map):
    with open('city_coding', 'w+') as f:
        for c in city_map:
            if c:
                f.write(c[0] + '\t' + c[1] + '\n')

    print('write done!')


def test():
    html_doc = get_location_html()
    city_map = parse_location(html_doc)


if __name__ == '__main__':
    #test()
    save_city_map(parse_location(html_doc=get_location_html()))

