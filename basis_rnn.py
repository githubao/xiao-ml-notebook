#!/usr/bin/env python
# encoding: utf-8

"""
@description: 用于理解rnn的代码

@author: pacman
@time: 2017/10/11 16:18
"""

import numpy as np
import tensorflow as tf

'''
mnist： 序列长度 * 样本的个数 * 向量长度
'''


def run():
    ' batch_size * step_size * embedding_size '
    x = np.random.randn(2, 3, 4)

    n_hidden = 8

    cell = tf.contrib.rnn.BasicLSTMCell(n_hidden)

    '''
    output: [batch_size, max_time, cell.output_size]
    last_states: [batch_size, state_size]
    '''
    outputs, last_states = tf.nn.dynamic_rnn(cell=cell, dtype=tf.float64, inputs=x)

    result = tf.contrib.learn.run_n({'outputs': outputs, 'last_states': last_states}, n=1, feed_dict=None)

    print(result[0])


def run2():
    x = np.random.randn(2, 10, 8)
    x[1, 6:0] = 0
    x_lengths = [10, 6]

    n_hidden = 64

    cell = tf.contrib.rnn.BasicLSTMCell(n_hidden)

    outputs, last_states = tf.nn.dynamic_rnn(cell=cell, dtype=tf.float64, sequence_length=x_lengths, inputs=x)

    result = tf.contrib.learn.run_n({'outputs': outputs, 'last_states': last_states}, n=1, feed_dict=None)

    print(result[0])


def main():
    run()


if __name__ == '__main__':
    main()
