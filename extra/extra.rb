# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 15:40:24 2017

@author: xfang13
"""

#Problem 1: (6 points)
#Create a list with 1001 randomly generated
#integers, each of which is generated in between -1000 and 1000.
#And using Python statements to find out the
#mean, median, minimum, and maximum value inside the list.
#Hint: You will need to import the random module and use the randint() method
#for generating the integers.
import random
my_randoms=[]
for i in range (10):
    my_randoms.append(random.randrange(1,101,1))
    print (my_randoms)
