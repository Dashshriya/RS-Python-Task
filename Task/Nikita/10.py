# -*- coding: utf-8 -*-
"""10

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NKNeOlFzhAleWJrsRGAuYxl33396mqv_
"""

X = [[1,2,3],
    [4,5,6],
    [7,8,9]]
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]


for i in range(len(X)):

   for j in range(len(X[0])):
       result[j][i]=X[i][j]

for r in result:
   print(r)