# -*- coding: utf-8 -*-
"""GAS_HOURLY SUPPLY_MOV_AVG_FILTER(1_2)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_OjVJx7D1i94gGNklf-qpgIcyIKROyzC
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("/content/drive/MyDrive/data/GHS.csv" ,sep=',' )

print(data)

def COVID(i):
    z = data['공급량'][i]
    return z

#인덱스는 0에서 부터 시작하기 때문에 n-1 을 해야 한다.
def mov_avg_filter(x_n, x_meas):
  n = len(x_n)
  for i in range(n-1):
    x_n[i] = x_n[i+1]
  x_n[n-1] = x_meas
  x_avg = np.mean(x_n)
  return x_avg, x_n

len(data)

n = 10
n_samples = 869
time_end = 10

dt = time_end / n_samples
time = np.arange(0, time_end, dt)
x_meas_save = np.zeros(n_samples)
x_avg_save = np.zeros(n_samples)

for i in range(n_samples):

    x_meas = COVID(i)
    
    if i == 0:
        x_avg, x_n = x_meas, x_meas * np.ones(n)
        print(x_meas * np.ones(n))
    else:
        x_avg, x_n = mov_avg_filter(x_n, x_meas)
        print(x_n)

    x_meas_save[i] = x_meas
    x_avg_save[i] = x_avg

plt.plot(time, x_meas_save, 'r*', label='COVID')
plt.plot(time, x_avg_save, 'b-', label='Moving average')
plt.legend(loc='upper left')
plt.title('Measured Altitudes v.s. Moving Average Filter Values')
plt.xlabel('Time [sec]')
plt.ylabel('Altitude [m]')
plt.savefig('/content/img')