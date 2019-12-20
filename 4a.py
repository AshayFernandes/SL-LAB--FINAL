# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 13:58:06 2019

@author: Ashay Fernandes
"""
lyst=[]

def celTOkel():
    val=int(input('enter the value of clesius'))
    res=val+273.15
    tup=("from celsius :",val,"To kelvin",res)
    lyst.append(tup)
def celTOfah():
    val=int(input('enter the value of clesius'))
    res=(val*(9/5))+32
    tup=("from celsius :",val,"To FAH",res)
    lyst.append(tup)
    
def kelTOfah():
    val=int(input('enter the value of kelvin'))
    res=(val-273.15)*(9/5)+32
    tup=("from kelvin:",val,"To fah",res)
    lyst.append(tup)

def rev():
       lyst1=[]
       for item in lyst:
        item=list(item)
        temp=item[0]
        item[0]=item[2]
        item[2]=temp
        temp=item[1]
        item[1]=item[3]
        item[3]=temp
        lyst1.append(tuple(item))
        print(lyst1)
def prin():
   print(lyst)

while True:
  print('1:celTOfah 2:celTOkel 3:kelTOFAh 4:print 5:reverse print 6:exit')
  i=int(input())
  if i==1:
    celTOfah()
  if i==2:
    celTOkel()
  if i==3:
    kelTOfah()
  if i==4:
     prin()
  if i==5:
    rev()
  if i==6:
     break        
       
    