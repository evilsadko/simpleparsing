# -*- coding:utf-8 -*-
import cv2
import sys
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

D = pd.read_csv('EURUSD-2019-02.csv')
arr = np.array(D)
print (arr[3,0], arr[3,1], arr[3,2], arr[3,3])
sort_by_date = np.sort(arr[:,1])
sort_by_price = np.sort(arr[:,2:])
print (sort_by_date.shape, sort_by_price.shape)
print (D)
history_limit = 1000


def watch(m, cur, min_history):
    n = np.random.randint(sort_by_date.shape[0] - min_history)
    target_bid, target_ask, other_bid, other_ask = generate_episode(n,cur)
    feature_span = get_features(target_bid, target_ask, other_bid, other_ask, m)
    normalized = (feature_span-feature_span.mean())/feature_span.std()
    return target_bid, target_ask, normalized



if __name__ == "__main__":
    print ("start")
