#encoding:utf-8
import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

f=open('')
df=pd.read_csv(f)
data=np.array(df[''])
data=data[::-1]#反转，是数据按日期先后顺序排列

#使用折线图展示data
plt.figure()
plt.plot(data)
plt.show()
normalize_data=(data-np.mean(data))/np.std(data)#标准化
normalize_data=normalize_data[:,np.newaxis]#增加维度


#*****************形成训练集*******************
#设置常量
time_step=20  #时间步
rnn_unit=10       #hidden layer units
batch_size=60     #每一批次训练多少个样例
input_size=1      #输入层维度
output_size=1     #输出层维度
lr=0.0006         #学习率
train_x,train_y=[],[]   #训练集
for i in range(len(normalize_data)-time_step-1):
    x=normalize_data[i:i+time_step]
    y=normalize_data[i+1:i+time_step+1]
    train_x.append(x.tolist())
    train_y.append(y.tolist())


#定义神经网络变量
X=tf.placeholder(tf.float32,[])