# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 06:46:48 2019

@author: Ashay Fernandes
"""

fh=open('3b.txt')
line=fh.read()
lyst=line.split()
dic={}
for i in lyst:
     dic[i]=dic.get(i,0)+1
     
sort_lyst=sorted(dic,key=lambda item:(item[1],item[0]),reverse=True)

if len(sort_lyst)<=10:
  print(sort_lyst)  

else:
    for i in range(10):
         print(sort_lyst[i],end=' ')
         
         