# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 06:15:01 2022

@author: Rakesh
"""

# 1.	A) list1=[1,5.5,(10+20j),’data science’].. Print default functions and parameters exists in list1.
# B) How do we create a sequence of numbers in Python.
# C)  Read the input from keyboard and print a sequence of numbers up to that number

list1=[1,5.5,(10+20j),"data science"]
def func (list1):
    print(list1)
    func(list1)

# B) How do we create a sequence of numbers in Python.
for i in range(10):
    print(i)
    
# C)  Read the input from keyboard and print a sequence of numbers up to that number   
for i in range(11):
    print(i)
    
# 2.	Create 2 lists.. one list contains 10 numbers (list1=[0,1,2,3....9]) and other 
# list contains words of those 10 numbers (list2=['zero','one','two',.... ,'nine']).
#  Create a dictionary such that list2 are keys and list 1 are values..

list1 = [0,1,2,3,4,5,6,7,8,9]
list2 = ['zero' , 'one', 'two', 'three' , 'four','five', 'six','seven', 'eight', 'nine']

print(dict(zip(list2, list1)))

# Consider a list1 [3,4,5,6,7,8]. Create a new list2 such that Add 10 to the even number and
#  multiply with 5 if it is odd number in the list1..

import numpy as pd
list2 = [num+10 if (num%2)==0 else num*5 for num in list1]
list2

# Write a simple user defined function that greets a person in such a way that :
#              i) It should accept both name of person and message you want to deliver.
#               ii) If no message is provided, it should greet a default message ‘How are you’

name = input("Hello, What's your name?")
print("Hello " + name+ " it's nice to meet you"+ "!")

def hello(name,message):
    print("hi",name,"your message:", message )
hello("Rakesh", 'how are you')



