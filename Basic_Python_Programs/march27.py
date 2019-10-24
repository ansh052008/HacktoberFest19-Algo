# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:09:36 2019

@author: Dell
"""

import math as m
m.pow(2,6)#returns 2^6


m.factorial(6)#returns 6!


m.floor(23.4)#returns an integer lower than the real number
#in this case 23

m.floor(23)#here also 23


m.fmod(6,4)#returns remainder when first arg divided by second arg.


m.modf(23.4)#returs integral and fractional part of the arg.
#here it returns (0.3999999999999986,23.0)
#here it returns an imprecise value of fractional part to 16 decimal digits.



area_of_a_circle=m.pi*(m.pow(5,2))#gives u area of a circle of radius 5


circumference_of_circle=m.tau*(5)#gives circumference of a circle of radius 5


import random as r
r.random()#returns a random floating number btw 0.0 and 1.0
r.choice([1,2,3,4,5,6])#returns random value from a sequence
"""
The sequence can be a list tupple dictionary etc.
"""
r.randint(1,9)#include last item
r.randrange(1,20,2)#don't include last item

l=[1,3,5,7,9]
r.shuffle(l)
print(l)




import tensorflow as tf
tf.__version__
