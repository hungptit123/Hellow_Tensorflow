import tensorflow as tf 

hellow = tf.constant("Hellow World Tensorflow!!!", dtype = tf.string, name = "Hellow")
c1 = tf.constant(5.0, dtype = tf.float32, name = "c1")
c2 = tf.constant(7.0, dtype = tf.float32, name = "c2")
op_add = tf.add(c1,c2)

with tf.Session() as sess:
	print ("value begin: ")
	print (sess.run([c1,c2,hellow]))
	print ("sum of c1 and c2: ")
	print (sess.run(op_add))
