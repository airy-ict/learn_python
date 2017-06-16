import tensorflow as tf

# 定义一个graph类，并在这张图上定义了foo与bar的两个变量，最后对这个值求和
graph = tf.Graph()
with graph.as_default():
    foo = tf.Variable(2, name="foo")
    bar = tf.Variable(3, name="bar")
    result = foo + bar
    # 并初始化所有变量
    initial = tf.global_variables_initializer()

print(result)  # 没有运算，输出：Tensor("add:0", shape=(), dtype=int32)

with tf.Session(graph=graph) as sess:
    sess.run(initial)
    res=sess.run(result)

print(res)


