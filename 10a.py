# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 12:26:50 2019

@author: Ashay Fernandes
"""
from functools import reduce
print('enter the 6 numbers to insert into list\n')
lyst=[]

while True:
    lyst.append(int(input()))
    if len(lyst)==6:
        print('you have netered 6 elements\n')
        break
    
lyst1=[x*3 for x in lyst] 
lsum=reduce(lambda x,y:x+y,lyst)
nlsum=reduce(lambda x,y:x+y,lyst1)

print('sums are'+str(lsum)+' '+str(nlsum))   