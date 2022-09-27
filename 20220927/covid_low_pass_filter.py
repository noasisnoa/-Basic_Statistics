# -*- coding: utf-8 -*-
"""COVID_LOW_PASS_FILTER.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fwIrmInwukQvhbE94_T--QT2s0LoAXeS
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import io

data = pd.read_csv('/content/drive/MyDrive/data/COVID19.csv',sep =',')

print(data)

def get_sonar(i):

  z =data['P'][i]
  return z

def low_pass_filter(x_meas,x_esti):
  x_esti = alpha * x_esti + (1 - alpha) * x_meas
  return x_esti

len(data)

#inout parameters
alpha = 0.7
n_samples = 9154
time_end = 10

dt = time_end / n_samples
time = np.arange(0, time_end, dt)
x_meas_save = np.zeros(n_samples)
x_esti_save = np.zeros(n_samples)

x_esti = None
for i in range(n_samples):
  x_meas = get_sonar(i)
  if i == 0:
    x_esti = x_meas
  else:
    x_esti = low_pass_filter(x_meas, x_esti)

  x_meas_save[i] = x_meas
  x_esti_save[i] = x_esti

plt.plot(time, x_meas_save, 'r*', label='Measured')
plt.plot(time, x_esti_save, 'b-', label='loww pass')
plt.legend(loc='upper left')
plt.title('Measured Altitudes v.s. Moving Average Filter Values')
plt.xlabel('Time [sec]')
plt.ylabel('Altitude [m]')
plt.savefig('/content/img')