# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 22:01:54 2019

@author: Ashay Fernandes
"""

dic={"H":"hydrogen","He":"helium","li":"lithium"}
while True:
    print('enter 1 to stop insetion 2:insert 3:length 4:searcg')
    i=int(input())
    if i==1:
        break
    if i==2:
      key=input('enter the key to be inserted')
      value=input('enter the value for the key')
      dic.update({key:value})
    if i==3:
      print(len(dic))
    if i==4:
       ele=input('enter the element to be searched')
       
       val=dic.get(ele,0)
       if val==0:
           print('not found')
       else:
         print('the element is '+val)   
         