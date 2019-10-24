# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:19:46 2019

@author: Dell
"""


#WAP to find squares of number using lambda function
l=[]
n=int(input("Enter number of elements in the list: "))
for i in range(n):
    x=int(input("Enter number: "))
    l.append(x)
print("Your list of squares is:",list(map(lambda x:x**2,l)))





#WAP to make fibonacci series using functions
def fibonacci(n):
    a=1
    b=1
    l=[1,1]
    for i in range(n):
        x=a+b
        l.append(x)
        a=b
        b=x
    print(l)
    print("Your first %d numbers from fibonacci series are:"%n,l[:n])
fibonacci(5)



def fib(n):
    a=0
    b=1
    l=[]
    for i in range(n+1):
        x=a+b
        print(a,b,x)
        a=b
        b=x
        
fib(5)



#program in class
f1=open('cse.txt','a')
f1.writelines("add list of lines or every sentences")
f1.close()#we need to close otherwise wontbe witten or modified
#to avoid close use "with open('file name','a/r/w/r+') as f" with :will take care of new line

f1.readlines()#Reads and gives list of sentences 
f1.read()#gives all lines in one sentence with spaces and enter as \n
#as we complete read cursor go to end
#to make it to 0 we use seek() method
#idexing of words start from 0 here also
f1.seek(0)
#readline: read only first line after cursor until \n
f1.readline()
f1.tell()

    

#classes
class student:
    sec='G'#properties of all elements in class
s=student()
s.sec
#self.university or student.university
#default value cant set.














import calendar
mycal=calendar.monthcalendar(2019,3)
for i in mycal:
    for j in i:
        if j in [2,3,5]:
            i[i.index(j)]="b"
print("\t\t\tMARCH 2019    ")
print("Mo\tTu\tWe\tTh\tFr\tSa\tSu")
for i in mycal:
    for j in i:
        if j==0:
            print(" ",end='\t')
        else:
            print(j,end='\t')
    print()
     


cal=calendar.month(2019,3)
print(cal)



f=open('C:\\Users\\Dell\\Desktop\\file.txt',"w")
f.write("Hi")
f.write(" Hello")
f.close()



f=open('C:\\Users\\Dell\\Desktop\\file.txt',"a")
f.write("Hey")
f.close()    