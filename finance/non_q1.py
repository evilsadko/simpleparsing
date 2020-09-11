from keras.optimizers import Adam
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM, CuDNNLSTM, BatchNormalization
from keras.callbacks import TensorBoard, ModelCheckpoint
from sklearn import preprocessing
from collections import deque
import tensorflow as tf
import pandas as pd
import numpy as np
import random
import time
import os

seq_len = 60  # последние 60 минут
period_predict = 3  # предсказать 3 минуты
#to_predict = 'BTC-USD'#'USD_RUB'
to_predict = 'ICE.BRN'
epochs = 1000
batch = 64
save_name = f"{to_predict}_{seq_len}_{int(time.time())}"

#def utils_1():
#    F = open("USD_RUB.csv", "r")#.read()
#    F1 = open("_USD_RUB.csv", "w")
#    for i in F:
#        i = i.split('\n')[0].split('","')
#        i = [o.replace('"',"").replace(',',".").replace("%", "") for o in i]
#        i = "{},{},{},{},{},{}\n".format(i[0],i[1],i[2],i[3],i[4],i[5])    
#        #print (i)
#        F1.write(i)
#    F1.close()

def score(current, future):
    #print (current, future)
    if float(future) > float(current):
        return 1  
    else:
        return 0


def test_lstm():
    KL = Sequential()
    KL.add(LSTM(128, activation='tanh', input_shape=(train_x.shape[1:]), return_sequences=True))
    KL.add(Dropout(0.2))
    KL.add(BatchNormalization())

    KL.add(LSTM(128, activation='tanh', input_shape=(train_x.shape[1:]), return_sequences=True))
    KL.add(Dropout(0.2))
    KL.add(BatchNormalization())

    KL.add(LSTM(128, activation='tanh', input_shape=(train_x.shape[1:])))
    KL.add(Dropout(0.2))
    KL.add(BatchNormalization())

    KL.add(Dense(32, activation='relu'))
    KL.add(Dropout(0.2))

    KL.add(Dense(2, activation="softmax"))
    return KL

def scaling(x):
    x = x.drop('future', 1)  
    for col in x.columns:
        #try:
                if col != 'target':
                    x[col] = x[col].pct_change() 
                    x.dropna(inplace=True)
                    x[col] = preprocessing.scale(x[col].values)  
        #except:
        #        pass
    x.dropna(inplace=True)  
    return x


def preprocess_data(x):
    prev_days = deque(maxlen=seq_len)
    sequential_data = []
    for i in x.values:
        #print (i)
        prev_days.append(i[:-1])  
        if len(prev_days) == seq_len:
            sequential_data.append([np.array(prev_days), i[-1]]) 
    random.shuffle(sequential_data)
    buys = []
    sells = []
    for seq, target in sequential_data:
        if target == 0:
            sells.append([seq, target])
        elif target == 1:
            buys.append([seq, target])
    lower = min(len(buys), len(sells))
    buys = buys[:lower]
    sells = sells[:lower]
    sequential_data = buys + sells
    random.shuffle(sequential_data)

    X = []
    y = []

    for seq, target in sequential_data:
        X.append(seq)
        y.append(target)

    return np.array(X), y


D = pd.DataFrame()
#currency = ['BTC-USD']##['BTC-USD']
#currency = ['ICE.BRN']
currency = ['ICE.BRN', 'EURUSD', 'USDRUB'] #, 'EURRUB' 'RUBEUR', 'RUBUSD', 
for ratio in currency:
    #dataset = f"BTC-USD.csv"#
    dataset = f"{ratio}.csv"
    #names=['time', 'low', 'high', 'open', 'close', 'volume']
    #names=['time', 'close', 'open', 'high', 'low', 'volume']
    df = pd.read_csv(dataset)#, names=['time', 'low', 'high', 'open', 'close', 'volume'])
    #df = pd.read_csv(dataset, names=['time', 'low', 'high', 'open', 'close', 'volume'])
##    df['close'] = df['close'].astype(float)
##    df['open'] = df['open'].astype(float)
##    df['low'] = df['low'].astype(float)
##    df['volume'] = df['close'].astype(float)
#    #print (df['close'].isnull().values.sum(), df['open'].isnull().values.sum(), df['high'].isnull().values.sum(),
#    #       df['low'].isnull().values.sum(), df['volume'].isnull().values.sum())
#----------------------------------------------------------------------->
    print (df)
#    df.rename(columns={'close': f'{ratio}_close', 'volume': f'{ratio}_volume'}, inplace=True)
#    df.set_index('time', inplace=True)
#    df = df[[f"{ratio}_close", f"{ratio}_volume"]]
    df.rename(columns={'<CLOSE>': f'{ratio}_close', '<VOL>': f'{ratio}_volume'}, inplace=True)
    df.set_index(['<DATE>', '<TIME>'], inplace=True)
    df = df[[f"{ratio}_close", f"{ratio}_volume"]]
    if len(D) == 0:
        D = df
    else:
        D = D.join(df)
    print (D)

D['future'] = D[f'{to_predict}_close'].shift(-period_predict)
D['target'] = list(map(score, D[f'{to_predict}_close'], D['future']))
print ("TERGET", D['target'], "\n",
       "FUTURE", D['future'])

# использовать последние 5% данных для тестирования
times = sorted(D.index.values)
last_5pct = int(-len(times) * 0.05)
last_10pct = int(-len(times) * 0.1) 

# сохраняйте данные проверки и обучения вместе при первом масштабировании
D = D[:last_5pct]
D = scaling(D)

# разделить на тренировку и проверку
training_df = D[:last_10pct]
validation_df = D[last_10pct:last_5pct]
# подготовка
train_x, train_y = preprocess_data(training_df)
val_x, val_y = preprocess_data(validation_df)

# статистика
print("train data:", len(train_x), train_x.shape, "\n",
      "validation:", len(val_x))
print ("===================train===================")
print ("don't buys:", train_y.count(0), "\n",
       "buys:", train_y.count(1))
print ("===================val===================")
print ("don't buys:", val_y.count(0), "\n",
       "buys:", val_y.count(1))

model = test_lstm()
opt = Adam(lr = 0.001, decay=1e-6)
model.compile(loss='sparse_categorical_crossentropy',
              optimizer=opt,
              metrics=['accuracy'])

tensorboard = TensorBoard(log_dir=f"logs/{save_name}")

# Сохранить
filepath = "{epoch:02d}_{val_acc:.3f}" 
checkpoint = ModelCheckpoint("models/{}.model".format(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max')) 
history = model.fit(train_x, train_y,
                    batch_size=batch,
                    epochs = epochs,
                    validation_data=(val_x, val_y),
                    callbacks=[tensorboard, checkpoint])
