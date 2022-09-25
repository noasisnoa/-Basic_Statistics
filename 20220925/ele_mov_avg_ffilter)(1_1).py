# -*- coding: utf-8 -*-
"""ELE_MOV_AVG_FFILTER)(1_1)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qWZYVcUL9dqOg57AbMHIH9HH1cCFlwsm
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Ozone Status in Seoul

data = pd.read_csv("/content/drive/MyDrive/data/ELE(1).csv",sep=',' )

print(data)

#인덱스는 0에서 부터 시작하기 때문에 n-1 을 해야 한다.
def mov_avg_filter(x_n, x_meas):
  n = len(x_n)
  for i in range(n-1):
    x_n[i] = x_n[i + 1]
    x_n[n-1] = x_meas
    x_avg = np.mean(x_n)

  return x_avg, x_n

n = 1
n_samples = 1126

time = np.arange(0, n_samples)
x_meas_save = np.zeros(n_samples)
x_mov_avg_save = np.zeros(n_samples)

for i in range(0,1126):
  x_meas = data
  if i == 0:
    x_avg, x_n = x_meas, x_meas * np.ones(n) # x_meas * np.ones(n)뭐가 나오는지 확인하세요
  else:
   x_avg, x_n = mov_avg_filter(x_n, x_meas)

   x_meas_save[i] = x_meas
   x_mov_avg_save[i] = x_avg

plt.plot(time, x_meas_save, 'r*', label='electricity consumption')
plt.plot(time, x_mov_avg_save, 'b-', label='avg')
plt.legend(loc='upper left')
plt.title('Measured Altitudes v.s. Moving Average Filter Values')
plt.xlabel('Time [sec]')
plt.ylabel('Altitude [m]')
plt.savefig('/content/img')