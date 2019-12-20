# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 11:55:26 2019

@author: Ashay Fernandes
"""

class student:
    
    def __init__(self):
        self.name=''
        self.age=0
        self.lyst=[]
        
    def accept(self):
        self.name=input('enter the name of the student\n')
        self.age=int(input('enter the age of student\n'))
        print('enter the marks in three subjects\n')
        for i in range(3):
            self.lyst.append(int(input()))
            
    def display(self):
        print("Name :{0}\nAGE :{1}\nmarks in 3 subjects:\n\tSubject 1 :{2[0]}\n\tSubject2 :{2[1]}\n\tSubject3 :{2[2]}\n".format(self.name,self.age,self.lyst))   
        
s1=student()
s2=student()
s1.accept()
s2.accept()
s1.display()
s2.display()        
        
        