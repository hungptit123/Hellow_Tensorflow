import tensorflow as tf 
import numpy as np 

g = tf.Graph()

with g.as_default():
	x = tf.Variable([.3], dtype = tf.float32, name = 'x')
	y = tf.placeholder(dtype = tf.float32, name = 'y')
	init = tf.global_variables_initializer()
	w = x*y
with tf.Session(graph = g) as sess:
	sess.run(init)
	# visualize graph on local host
	# open command: tensorboard --logdir='tf.logs'
	writer = tf.summary.FileWriter('tflogs', sess.graph)
	print (sess.run(w, feed_dict = {y: [2.4, 3.0]}))