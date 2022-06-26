# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 06:41:42 2022

@author: Rakesh
"""

##1.	Construct 2 lists containing all the available data types  (integer, float, string, complex and Boolean) and do the following..
#a.	Create another list by concatenating above 2 lists
#b.	Find the frequency of each element in the concatenated list.
#c.	Print the list in reverse order####

list1= [22 ,45 ,68 , 12.5 , 6.8 ,"rakesh" , "data science" , 3j , 3+4j ,True ,False ]
list2= [55 , 89 , 34 , 2.2 , 5.5 , "assignment" , "python" , 6j , 2+5j , True , False]

##a = Create another list by concatenating above 2 lists##

list3 = list1 + list2
print(list3)  
#b.	Find the frequency of each element in the concatenated list.
list1= [22 ,45 ,68 , 12.5 , 6.8 ,"rakesh" , "data science" , 3j , 3+4j ,True ,False ]
list2= [55 , 89 , 34 , 2.2 , 5.5 , "assignment" , "python" , 6j , 2+5j , True , False]

list3.count(True)
list3.count(False)
list3.count(25)
list3.count(45)
list3.count(68)
list3.count(12.5)
list3.count(6.8)
list3.count("rakesh")
list3.count("data science")
list3.count(3j)
list3.count(3+4j)
list3.count(55)
list3.count(89)
list3.count(34)
list3.count(2.2)
list3.count(5.5)
list3.count("assignment")
list3.count("python")
list3.count(6j)
list3.count(2+5j)

#c.	Print the list in reverse order####

list1= [22 ,45 ,68 , 12.5 , 6.8 ,"rakesh" , "data science" , 3j , 3+4j ,True ,False ]
list2= [55 , 89 , 34 , 2.2 , 5.5 , "assignment" , "python" , 6j , 2+5j , True , False]
##if you want reverse for list3 , below is coding
list3 = list1 + list2
print(list3)
list3.reverse()
print(list3)
##other wise individual lists reverse is below
list1.reverse()
print(list1)
list2.reverse()
print(list2)

##2.	Create 2 Sets containing integers (numbers from 1 to 10 in one set and 5 to 15 in other set)##
#a.	Find the common elements in above 2 Sets.##
#b.	Find the elements that are not common.##
#c.	Remove element 7 from both the Sets.##

set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {5,6,7,8,9,10,11,12,13,14,15}
lis=set1.intersection(set2)
lis

#a.	Find the common elements in above 2 Sets.##
intersection_as_list= list(lis)
print(intersection_as_list)
#b.	Find the elements that are not common.##
set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {5,6,7,8,9,10,11,12,13,14,15}
lis = set1 - set2
lis

##c.	Remove element 7 from both the Sets##
set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {5,6,7,8,9,10,11,12,13,14,15}

set1.remove(7)
set1
set2.remove(7)
set2

##3.	Create a data dictionary of 5 states having state name as key and number of covid-19 cases as values.
##a.	Print only state names from the dictionary####
covid19_cases = {'Maharastra' : 7912462,'Kerala':6580411,'Madhya pradesh':1043178 ,'Karnataka': 3956749, 'Kerala':6580411}
covid19_cases.keys()
##b.	Update another country and it’s covid-19 cases in the dictionary.
covid19_cases['USA'] = 87549420
print(covid19_cases)  


