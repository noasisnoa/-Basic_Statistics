# -*- coding: utf-8 -*-
"""comfidence level.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oYHe0Zk06AZWYlAyCx0YFXGjBxVfJkgi
"""

#신뢰도 구간 
sample1 = [5, 10, 17, 29, 14, 25, 16, 13, 9, 17]
sample2 = [21, 22, 27, 19, 23, 24, 20, 26, 25, 23]

import scipy.stats as st
import numpy as np

df = len(sample1)-1  #자유도 : 샘플 개수 - 1
mu = np.mean(sample1)# 표본 평균
s = np.std(sample1) #표본 표준 편차
se = st.sem(sample1) #표준 오차, s/mnp.sqrt(mu)
#표본 분산
ss = np.std(sample1)*(df+1)/df
ses = ss/np.sqrt(df)

print('표준평균 =', mu)
print('표준 표준편차 = ', s)
print('표준오차 = ', se)
print('표본 분산 =', ss)
print('표준오차 = ', ses)
print(s/np.sqrt(mu))
# 95%신뢰도 구간 구하기

x = [10, 1, 10, 9.8, 10, 5, 9, 7, 10, 1, 9, 9, 10, 2, 10, 3, 9, 9]
df = len(x)-1
print(len(x))
x1 = np.array(x)
mean = x1.mean()
std=x1.std()
print('평균', mean)
print('표준편차', std)

import numpy as np
import matplotlib.pyplot as plt
import scipy as scipy
import scipy.stats
import scipy as sp

 
def show_pdfcdf(rv, m,s):
  mm = m
  ss = 6 * s
  xx = np.linspace(mm-ss, mm + ss, 200)
  pdf = rv.pdf(xx)
  cdf = rv.cdf(xx)

  plt.grid(True)
  plt.plot(xx, pdf)
  plt.plot(xx, cdf)
  plt.title(f'Norm(m={m}, s^2={s*s: 3f} Pdf & Cdf')
  plt.savefig('dist.png')
  plt.show()

m, s = 70, 4.9/np.sqrt(49)
rv = sp.stats.norm(m, s) 

show_pdfcdf(rv, m, s)

x1= 70.7
print(f'Prob ({x1}) =',rv.cdf(x1))
print(f'Prob (1-{x1}<= x  =', 1- rv.cdf(x1))

low_interval = m -1.96 * s
upper_interval = 1.96 * s
print(f"interval {low_interval} - {upper_interval}")