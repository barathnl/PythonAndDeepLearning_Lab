from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)


import tensorflow as tf

learning_rate = 0.01
training_iteration = 30
batch_size = 100
display_step = 2

data1 = tf.placeholder("float", [None, 784]) # mnist data image of shape 28*28=784
data2 = tf.placeholder("float", [None, 10]) # 0-9 digits recognition => 10 classes

wgt = tf.Variable(tf.zeros([784, 10]))
bias = tf.Variable(tf.zeros([10]))

logmodel = tf.nn.softmax(tf.matmul(data1, wgt) + bias) # Softmax


cost_function = -tf.reduce_sum(data2*tf.log(logmodel))

optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost_function)


init = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)

    writer = tf.summary.FileWriter('./graphs/linear_reg', sess.graph)

    for iteration in range(training_iteration):
        avg_cost = 0.
        total_batch = int(mnist.train.num_examples/batch_size)
        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            sess.run(optimizer, feed_dict={data1: batch_xs, data2: batch_ys})
            avg_cost += sess.run(cost_function, feed_dict={data1: batch_xs, data2: batch_ys})/total_batch
        if iteration % display_step == 0:
            print ("epoch:", '%04d' % (iteration + 1), "cost=", "{:.9f}".format(avg_cost))

    writer.close()
    print ("Tuning completed!")
    predictions = tf.equal(tf.argmax(logmodel, 1), tf.argmax(data2, 1))
    accuracy = tf.reduce_mean(tf.cast(predictions, "float"))
print ("Accuracy:", accuracy.eval({data1: mnist.test.images, data2: mnist.test.labels}))