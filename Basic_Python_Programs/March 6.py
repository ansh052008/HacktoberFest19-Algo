# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 10:38:56 2019

@author: Dell
"""


print('Helo \'it is me')#slash used to make' as string not end of quote
def record(name,score=0):#here score is keyword as it is given a key value beforehand
    print("%s scored %s"%(name,score))
record(score=3, name="Jill")

#args and kwargs using * , **: used to input multiple arguments within one variate argument
#args gives tupple kwargs give dictionary.

print("a:{0} , b:{1}".format(1,2))# {0} is placeholder in format(brackets)



#__doc__ :prints documentation /comments inside a function.
def hello(name="everybody"):
    """Greets everybody"""
    print("hello",name)
print("The docstring of function hello or comments in hello:",hello.__doc__)

def square(x,y):
    return x*x,y*y
a,b=square(1,2)



#lambda arguments:expression  #annonymous or namelessfunctions or lambda function for short time period

double=lambda x:x*2
print(double(5))


"""Questions on Lambda function"""
#Write a lambda function to convert celsius to fahrenheit
fc=lambda c:1.8*c+32
print(fc(38))


#Write a program using lambda function to display odd numbers from a list
l=[1,2,3,4,5,6,7,8,9,10]
list_of_odd_num=list(filter(lambda x:x%2!=0,l))
"""
1. Filter is a higher order function which takes a function and a list as an argument.
2. The filter function will return numbers like in zip function for whom the function holds true.
3. There is also a map function which returns the values evaluated by the function and take each element 
   of a list as an argument.
"""
print(list_of_odd_num)

