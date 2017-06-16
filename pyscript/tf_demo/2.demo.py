""" 
Please note, this code is only for python 3+. If you are using python 2+, please modify the code accordingly. 
"""  
import tensorflow as tf  
import numpy as np  
  
  
def add_layer(inputs, in_size, out_size, n_layer, activation_function=None):  
    # 添加一层并返回该层的输出
    layer_name = 'layer%s' % n_layer  
    with tf.name_scope(layer_name):  
        with tf.name_scope('weights'):  
            Weights = tf.Variable(tf.random_normal([in_size, out_size]), name='W')  
            tf.summary.histogram(layer_name + '/weights', Weights)  
        with tf.name_scope('biases'):  
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, name='b')  
            tf.summary.histogram(layer_name + '/biases', biases)  
        with tf.name_scope('Wx_plus_b'):  
            Wx_plus_b = tf.add(tf.matmul(inputs, Weights), biases)  
        if activation_function is None:  
            outputs = Wx_plus_b  
        else:  
            outputs = activation_function(Wx_plus_b, )  
        tf.summary.histogram(layer_name + '/outputs', outputs)  
        return outputs  
  
  
# Make up some real data  
x_data = np.linspace(-1, 1, 300)[:, np.newaxis]  
noise = np.random.normal(0, 0.05, x_data.shape)  
y_data = np.square(x_data) - 0.5 + noise  
  
# 定义网络输入的占位符  
with tf.name_scope('inputs'):  
    xs = tf.placeholder(tf.float32, [None, 1], name='x_input')  
    ys = tf.placeholder(tf.float32, [None, 1], name='y_input')  
  
# 添加隐藏层 
l1 = add_layer(xs, 1, 10, n_layer=1, activation_function=tf.nn.relu)  
# 添加输出层  
prediction = add_layer(l1, 10, 1, n_layer=2, activation_function=None)  
  
# 损失函数
with tf.name_scope('loss'):  
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),  
                                        reduction_indices=[1]))  
    tf.summary.scalar('loss', loss)  

# 训练
with tf.name_scope('train'):  
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)  
  
sess = tf.Session()  
merged = tf.summary.merge_all(key='summaries') 
writer = tf.summary.FileWriter("logs/2/", sess.graph)  
# 运算
sess.run(tf.initialize_all_variables())  
  
for i in range(1000):  
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})  
    if i % 50 == 0:  
        result = sess.run(merged, feed_dict={xs: x_data, ys: y_data})  
        writer.add_summary(result, i)  

