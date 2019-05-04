import tensorflow as tf 
from tensorflow.python.client import device_lib

# print (device_lib.list_local_devices())
# enable the logging of varialbe placement by define a config object.
tf.reset_default_graph()

with tf.device('/device:CPU:0'):
	# define model parameter
	w = tf.get_variable(name = 'w', initializer = [.3], dtype = tf.float32)
	x = tf.placeholder(name = 'x', dtype = tf.float32)
	y = w*x

config = tf.ConfigProto()
config.log_device_placement = True
# config.
init = tf.global_variables_initializer()

with tf.Session() as sess:
	sess.run(init)
	print ("output: ", sess.run(y, feed_dict = {x:[2.0, 3.0]}))


