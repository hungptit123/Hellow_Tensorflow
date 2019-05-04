import tensorflow as tf 
import numpy as np 

c = tf.Variable(5.0, tf.float32)
d = tf.constant(6.0, tf.float32)
h = tf.placeholder(tf.float32)
c = c+d
init = tf.global_variables_initializer()

with tf.Session() as sess:
	sess.run(init)	
	print (sess.run(c))