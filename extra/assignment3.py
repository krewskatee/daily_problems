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
for i in range (1001):
    my_randoms.append(random.randint(-1000, 1000))
print (my_randoms)

average = 0
for i in my_randoms:
    average = average + i
print("The average of the list is %f." % (average/1001))

minimum = 1001
for i in my_randoms:
    if i < minimum:
        minimum = i
print("The minumum of the list is %i." % (minimum))

maximum = -1001
for i in my_randoms:
    if i > maximum:
        maximum = i
print("The maximum of the list is %i." % (maximum))

#Problem 2: (10 points)
#Write the procedure that computes the muliplication of two matrices
#Your code should work for any size matrices, assuming that
#the total number of columns in the first matrix matches the total number of
#rows in the second matrix
#Use the following matrices as testing data
matrix_A = [[1,2,3],[4,5,6]]
matrix_B = [[1,2,3,4],[4,5,6,7],[7,8,9,10]]
def multiply_matrix(X, Y):
    result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
    return result

print(multiply_matrix(matrix_A, matrix_B))


#Problem 3: (6 points)
#Implement the insertion-sort algorithm
#Pseudo code:
#Input: A Python list, A, with unsorted numbers
#Output: A sorted list, A, where the numbers are sorted ascendingly
#for i from 1 to n (n is the length of A)
#   assign i-1 to j
#   assign A[i] to key
#   while j is greater than or equal to 0 and A[j] is greater than key
#       assign A[j] to A[j+1]
#       decreament j by 1
#   assign key to A[j+1]
A = [random.randint(0,1000) for i in range(50)]

for i in range(1, len(A)):
    j = i-1
    key = A[i]
    while j >= 0 and A[j] > key:
        A[j+1] = A[j]
        j = j-1
        A[j+1] = key
print(A)

#Problem 4: (8 points)
#Write Python statements that create a dictionary of word counts.
#Specifically, keys of the dictionary are words; values of the dictionary
#are the number of occurances of the words
#For example, given s = 'go go hurry up', the dictionary, D, should be like
# {'go':2, 'hurry':1, 'up':1}
s = '''
Deep learning also known as deep structured learning hierarchical learning or deep machine learning is a branch of machine learning
based on a set of algorithms that attempt to model high level abstractions in data In a simple case there might be two sets of neurons
ones that receive an input signal and ones that send an output signal When the input layer receives an input it passes on a modified
version of the input to the next layer In a deep network there are many layers between the input and output and the layers are not made
of neurons but it can help to think of it that way allowing the algorithm to use multiple processing layers composed of multiple linear
and non-linear transformations
'''
words = s.split()

counts = {}
for i in words:
  counts[i] = counts.get(i, 0) + 1
print(counts)
