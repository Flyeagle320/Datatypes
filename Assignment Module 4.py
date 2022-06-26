# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 06:15:20 2022

@author: Rakesh
"""

# 1.	 Take a variable ‘age’ which is of positive value and check the following:
# a.	If age is less than 10, print “Children”.
# b.	If age is more than 60 , print ‘senior citizens’
# c.	 If it is in between 10 and 60, print ‘normal citizen’

age= int(input("Enter your Age : "))
if age<10:
    print("Children")
elif age>60:
    print("Senior Citizen")
else:
    print("Normal Citizen")
   
# 2.	Find  the final train ticket price with the following conditions. 
# a.	If male and sr.citizen, 70% of fare is applicable
# b.	If female and sr.citizen, 50% of fare is applicable.
# c.	If female and normal citizen, 70% of fare is applicable
# d.	If male and normal citizen, 100% of fare is applicable
import pandas as pd
gender = str(input("Male or Female : "))
age1  = int(input("Enter your age : "))
if gender =='Male' and age1>=60:
    print("70% of fare is applicable")
elif gender=='Female' and age1>=60:
    print("50% of fare is applicable")
elif gender== 'Male' and age1<60:
    print("100% of fare is applicable")
if gender == 'Female' or age1<60:
    print("70% of fare is applicable")
   
 
      
# 3.	Check whether the given number is positive and divisible by 5 or not.      
    
number = float(input(" Please Enter any Positive Integer : "))
if number % 5 == 0:
   print("Given Number {0} is Divisible by 5 ".format(number))
else:
   print("Given Number {0} is Not Divisible by 5 ".format(number))




    
    
 
        