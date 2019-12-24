# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 06:46:48 2019

@author: Ashay Fernandes
"""

fh=open('3b.txt')
line=fh.read()
lyst=line.split()
dic={}

for x in lyst:
    dic[x]=dic.get(x,0)+1
    
lyst1=sorted(dic.items(),key=lambda x:(x[1],x[0]),reverse=True)
print(dic)
if len(lyst1)<=10:
   for i in range(len(lyst1)):
       print(lyst1[i][0])
       
length=[len(x) for x in list(dic.keys())]
import functools
su=functools.reduce(lambda x,y:x+y,length)/len(length)
odd=[x*x for x in length if x%2!=0]       