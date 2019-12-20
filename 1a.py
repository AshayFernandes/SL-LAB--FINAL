# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 22:37:00 2019

@author: Ashay Fernandes
"""
lyst=[]

while True:
  print('enter elementemt to be inserted or enter "stop" to stop inserting')
  ele=input()
  if ele=='stop':
      break
  else:
    lyst.append(ele)
lyst1=lyst[:]
lyst1.sort()
print
while True:
     print('1:insert 2:delete 3:present 4:maxmin 5:exit')
     i=int(input())
     if i==1:
         lyst.append(input('enter the element'))
     if i==2:
         try:
           lyst.remove(input('enter the element'))
         except ValueError:
             print('not found')
     if i==3:
         ele=input('enter the element')
         for item in lyst:
             if ele==item:
                 print('found')
                 break
             else:
                 print('not found')
                 break
     if i==4:
         lyst1=lyst[:]
         lyst1.sort()
         print('min{0} and max{1}'.format(lyst1[0],lyst1[len(lyst1)-1]))
     if i==5:
         break
            
    
