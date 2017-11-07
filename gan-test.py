import tensorflow as tf
import numpy as np

Dg_logits = tf.constant([-2.3, 2.0, -4.5, 2.2], dtype=tf.float32, shape=(4, ))

#with tf.variable_scope('D') as scope:

g_loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=Dg_logits, labels=tf.zeros_like(Dg_logits)))

#g_loss = tf.reduce_mean(-tf.log(Dg_logits))
Dx_logits = tf.constant([-3.0, -4.9, 2.1, 0.8], dtype=tf.float32, shape=(4, 1))
d_loss_real = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=Dx_logits, labels=tf.zeros_like(Dx_logits)))
d_loss_fake = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=Dg_logits, labels=tf.zeros_like(Dg_logits)))

d_loss = d_loss_real + d_loss_real

with tf.Session() as sess:
    g_L = g_loss.eval()
    print(g_L)
    d_L = d_loss.eval()
    print(d_L)


