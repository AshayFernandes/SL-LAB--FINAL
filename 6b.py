# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 13:58:06 2019

@author: Ashay Fernandes
"""

class sentence_reverse:
    def __init__(self,string=''):
        self.string=string
        self.v=0
        self.rev=''
    def reve(self):
        lyst=self.string.split()
        lyst.reverse()
        self.rev=' '.join(lyst)
        print(self.rev)
        for x in self.rev.lower():
            if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
                self.v+=1
        print(self.v)        
    def dis(self,o1,o2):
        dic={ self.rev:self.v,o1.rev:o1.v,o2.rev:o2.v}
        print(dic)
        lyst1=sorted(dic.items(),key=lambda item:(item[1],item[0]),reverse=True)
        print(lyst1)
        for item in lyst1:
           print(item[0]) 

      
print('insert 3 string')
string1=input()
string2=input()
string3=input()
s1=sentence_reverse(string1)
s1.reve()
s2=sentence_reverse(string2)
s3=sentence_reverse(string3)
s2.reve()
s3.reve()
s1.dis(s2,s3)               
            
        
        
        