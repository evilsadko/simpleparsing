# -*- coding:utf-8 -*-
import tensorflow.contrib.slim as slim
import tensorflow as tf
import cv2
import sys
import random
import numpy as np
import matplotlib.pyplot as plt
sess = tf.InteractiveSession()

ACTIONS = None

#def RnnNetwork():

#def CnnNetwork():

#def get_batch():

def train():
    #x, R = RnnNetwork/CnnNetwork
    a = tf.placeholder("float", [None, ACTIONS])
    y = tf.placeholder("float", [None])
    R_action = tf.reduce_sum(tf.multiply(R, a), reduction_indices=1) #действие считывания
    cost = tf.reduce_mean(tf.square(y - R_action))
    #train_step = tf.train.AdamOptimizer(1e-6).minimize(cost)

    do_nothing = np.zeros(ACTIONS)
    do_nothing[0] = 1
    x_t, r_0, control_action = get_batch(do_nothing)
    #x_t = np.array([])
    s_t = np.stack((x_t, x_t, x_t, x_t), axis=2)

    saver = tf.train.Saver()
    sess.run(tf.initialize_all_variables())
    checkpoint = tf.train.get_checkpoint_state("saved_networks")
    if checkpoint and checkpoint.model_checkpoint_path:
        saver.restore(sess, checkpoint.model_checkpoint_path)

    epsilon = 0.001
    t = 0
    while True:
        R_t = R.eval(feed_dict={x : [s_t]})[0]
        a_t = np.zeros([ACTIONS])
        action_index = 0
        if t % 1 == 0:
            if random.random() <= epsilon:
                print("----------Random Action----------")
                action_index = random.randrange(ACTIONS)
                a_t[random.randrange(ACTIONS)] = 1
            else:
                action_index = np.argmax(R_t)
                a_t[action_index] = 1
        else:
            a_t[0] = 1 

        if epsilon > 0.0001 and t > 100000.:
            epsilon -= (0.001 - 0.0001) / 2000000.

        # выполнить выбранное действие и наблюдать за следующим состоянием и вознаграждением
        x_t1_, r_t, control_action = get_batch(a_t)
        #s_t1 = np.append(x_t1, s_t[:,:,1:], axis = 2)
        s_t1 = np.append(x_t1, s_t[:, :, :3], axis=2)

        # сохранить переход в D
        D.append((s_t, a_t, r_t, s_t1, control_action))
        if len(D) > 50000:
            D.popleft()

        if t > 100000.:
            # образец мини-пакета для обучения
            minibatch = random.sample(D, 30)

            s_j_batch = [d[0] for d in minibatch]
            a_batch = [d[1] for d in minibatch]
            r_batch = [d[2] for d in minibatch]
            s_j1_batch = [d[3] for d in minibatch]

            y_batch = []
            R_j1_batch = R.eval(feed_dict = {s : s_j1_batch})
            for i in range(0, len(minibatch)):
                control_action = minibatch[i][4]
                if control_action:
                    y_batch.append(r_batch[i])
                else:
                    y_batch.append(r_batch[i] + 0.99 * np.max(R_j1_batch[i]))

            train_step.run(feed_dict = {
                y : y_batch,
                a : a_batch,
                s : s_j_batch}
            )

        s_t = s_t1
        t += 1

#http://stanford.edu/class/msande448/2019/Final_reports/gr2.pdf
#https://www.integral.com/
#https://www.truefx.com/truefx-historical-downloads/
#nerevaren:qwertyqaz
if __name__ == "__main__":
    print ("start")
