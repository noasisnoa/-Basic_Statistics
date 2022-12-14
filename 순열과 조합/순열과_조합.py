# -*- coding: utf-8 -*-
"""순열과 조합.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1762BM769Ao-Yt42D4Gt7pxSpPZjpPFbe
"""

!python  --version

!wget https://www.python.org/ftp/python/3.9.9/Python-3.9.9.tgz
!tar xvfz Python-3.9.9.tgz
!Python-3.9.9/configure
!make
!sudo make install

!python  --version

import math

def permutatuins_count(n, r):
  return math.factorial(n) // math.factorial(n-1)

print(permutatuins_count(4, 2))

def combination_count(n, r):
  return math.factorial(n) // math.factorial(n -r)*math.factorial(r)

print(combination_count(4, 2))

def permutation_with_repetition_count(n, r):
  return math.pow(n,r)
print(permutation_with_repetition_count(4, 2))

def permutation_with_repetition_count2(n, r):
  a = n+r -1
  b = r
  return math.factorial(a)//(math.factorial(a-b)*math.factorial(b))
print(permutation_with_repetition_count2(4,2))

"""프린트 5번은 순열"""

from itertools import permutations

arr = [ 1, 2, 3,]
print(list(permutations(arr, 2)))

def gen_permutations(arr, n):

  result = []

  if n == 0:
    return [[]]

  for i, elem in enumerate(arr):
    for P in gen_permutations(arr[:i] + arr[i+1:], n-1):
      print(i, P)
      result += [[elem]+P]

  return result

for i, letter in enumerate(['A', 'B', 'C'], start = 1): 
  print(i, letter)

#(여기 아래부터) 다시해보기

arr = [1, 2, 3]
print(gen_permutations(arr, 2))

#외우세요 시험을 볼 것입니다. 

def gen_permutations(arr, n):

  result = []

  if n == 0:
    return [[]]

  for i, elem in enumerate(arr):
    print(i, elem)
    print(arr[:i] + arr[i+1:])
    for P in gen_permutations(arr[:i] + arr[i+1:], n-1):
      print(P)
      result += [[elem]+P]
    print("_______________")
  return result

arr = [3,4,5]
print(gen_permutations(arr, 2))

"""#재귀함수"""

def hello(count):
  if count ==0:
    return

  print('Hello, world', count)

  count -= 1   #countfmf 1 감소시킨 뒤
  hello(count) #다시 hello에 넣음