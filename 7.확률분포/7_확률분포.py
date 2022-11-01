# -*- coding: utf-8 -*-
"""7.확률분포.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FSLJU5In6qfFZd6jbpxY0Z79gdnb-q-h
"""

import sys
import math
print(sys.version)

def combination_count(n, r):
  return math.factorial(n) // (math.factorial(n -r)*math.factorial(r))

# 스스로 완성
n = 0

print("동전을 4번 던져서 n개")
p = combination_count(9, 3)

print("n을 입력하세요")
n = int(input())
if n>4:
  print("다시입력하세요.")
  n = int(input())
  
  if(n == 1):
    i = combination_count(4,3)
    print(i/p)
  elif(n==2):
    i = combination_count(4,2) * combination_count(5,1)
    print(i/p)
  elif(n==3):
    i = combination_count(4,1) * combination_count(5,2)
    print(i/p)
  elif(n==4):
    i = combination_count(4,0) * combination_count(5,3)
    print(i/p)
  else:
    print('연산을 할 수 없습니다.')

print("빨간공 r개, 파란공 b개가 들어있는 주머니에서 n개의 공으르 꺼내려 한다.")
print("뽑힌 공 중 파란공의 개수를 확률 변수 x라고 했을 때 x의 확률분포를 구하여라")
5
b=0
r=0
n=0
X=0.0
print("빨간공의 개수를 입력하시오")
r = int(input())
print("파란공의 개수를 입력하세요")
b = int(input())
print("던질 횟수를 입력하세요")
n = int(input())

sum = 0
avg = 0
var = 0

for i in range(n+1):
  result = combination_count(r,n-i) * (combination_count(b,i) / combination_count(r+b,n))
  sum += result
  avg += result*i
  print("P(",i,") = ", result)
print("Psum = ", sum)
print("avg = ", avg)

for i in range(n+1):
  result = combination_count(r,n-i) * (combination_count(b,i) / combination_count(r+b,n))
  var +=(i-avg)*(i-avg)*result
print("var=",var)