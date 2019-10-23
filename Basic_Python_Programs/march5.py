# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:49:48 2019

@author: Dell
"""

#Q.1 Write a function to display sum of all the integers if present in a string.
def sumofint(s):
    l=s.split()
    print(l)
    l1=[]
    for i in l:
        for k in i:
            print (k)
            if ord(k) in range(48,58):
                l1.append(int(i))
    print(l1)
    l2=list(set(l1))
    print(sum(l2))
x=input()
sumofint(x)          


#take two argument from user arg1=string arg2=word,function  covert that word to "pagal hai kya"
def phk(s,w):
    s.lower()
    w.lower()
    l=s.split()
    for i in l:
        if i==w:
            l[l.index(i)]="Pagal hai kya"
    s1=' '.join(l)
    print(s1)
a=input("Enter string: ")
b=input("Enter word to be replaced: ")
phk(a,b)