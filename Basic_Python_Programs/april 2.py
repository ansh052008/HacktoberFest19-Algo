# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 10:44:31 2019

@author: Dell
"""

#multiple and single inheritance
#its a kind of hierarchy


#base class
#derievd class ha sall properties of base class as well as new class


#list is also a class
class stack(list):
    push=list.append
st=stack()
st.pop()#we can use

#what is override in inheritance.

"""
polymorphism
"""
"""
static and final keywords / scope of a class
public private and protected keywords.


public: global
private: only in class
protected: class and subclass



all members in class in python are public.
"""


#for protected put self._name=name



"""
for private use self.__name=name"""

"""
e1._employee_salary
"""








class notebook:
    def __init__(self,type):
        self.type=type
    def func(self):
        print("I'm a notebook")

class company(notebook):
    def __init__(self,company):
        self.company=company
    def f(self):
        print("I belong to the this comapny",company)
