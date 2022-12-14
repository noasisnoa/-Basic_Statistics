# -*- coding: utf-8 -*-
"""numpy 를 이용한 행렬 연산.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yPKXHAcgO8arQ39KMrydHH0-MOD2YFQe

# 행렬의 정의와 determinant
"""

import numpy as np
#np.array를 사용하여 2*2 행렬 생성
d_array = np.array([[2, 5],
                   [1, 3]])

d_array_det = np.linalg.det(d_array)
#linalg 행렬 대수
print(d_array_det)

"""#역행렬"""

import numpy as np

d_array_inv = np.linalg.inv(d_array)
print(d_array_inv)

"""# 단위 행렬"""

#대각 행렬 만드는 함수 EYE
print(np.eye(3))

print(np.transpose(d_array))
print(d_array.transpose())
print(d_array.T) # .임

"""## Linear Algebra 2. 대각행렬

"""

x = np.arange(9).reshape(3, 3)
print(x)

np.diag(x)

np.diag(np.diag(x))

"""# 내적 : 두개의 행렬을 곱하 것

"""

a = np.arange(4).reshape(2, 2)
print(a)

#헹렬 원소의 곱
print(a * a)

"""# 대각합"""

b = np.arange(16).reshape(4, 4)
 print(b)

np.trace(b)