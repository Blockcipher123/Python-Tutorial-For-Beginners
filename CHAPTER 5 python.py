# ***************************************************************************************************************************************************************************
# **************************************************************CH-5*************************************************************************************************************
# ***************************************************************************************************************************************************************************
# ***************************************************************************************************************************************************************************
# ***************************************************************************************************************************************************************************
# ***************************************************************************************************************************************************************************
# ***************************************************************************************************************************************************************************



#                                               list
# intro list
# you can store any thing in list int, float, string
number = [1,2,5,5,8]
print(number[4])


word = ['name', 'Block', 'cipher']
print(word[:1])


mixed = ['word', 'gaurav', 23, 24, 2.3, 2.3, None]
print(mixed[-1])


mixed[1:] = 'Block_cipher'
print(mixed)


#                                                   Add data to list
print('fruits Name')
fruits = ['mango', 'apple', 'grapes', 'lichi']
fruits.append('pine apple')
print(fruits)


vegetables = []
print('vevegetables Name')
fruits.append('Potato')
fruits.append('onion')
fruits.append('ladifinger')
fruits.append('cabage')
print(fruits)

#													 More method to add data
# inseret method
# how to join(concotenate) two list
# extend method 
# difference between append and extend method


# inseret method
fruits1 = ['mango', 'grapes']
fruits1.insert(3, 'apple')
print(fruits1)

# concotenate
fruits1 = ['mango', 'grapes']
fruits2 = ['apple', 'banana']
fruits = fruits1 + fruits2
print(fruits)

# extent method
fruits1 = ['mango', 'grapes']
fruits2 = ['apple', 'banana']
fruits1.extend(fruits2)
print(fruits1)
print(fruits2)

#  difference between append and extend method
fruits1 = ['mango', 'grapes']
fruits2 = ['apple', 'banana']
fruits1.append(fruits2)
print(fruits1)
print(fruits2)

#                                    Delete data from list
# cammand method to delete data from list
Boys = ['shivam', 'ashwani', 'aman', 'ram', 'rohit']
# pop method
Boys.pop(3)
print(Boys)

# del method

Boys = ['shivam', 'ashwani', 'aman', 'ram', 'rohit']

del Boys[1]
print(Boys)

# remove method
Boys = ['shivam', 'ashwani', 'aman', 'ram', 'rohit']
Boys.remove('ram')
print(Boys)

# Data add 
# append, extend, insert
# Delete data 
# pop, remove, del

# 														In keybord with list
Fruits = ['orange', 'pear', 'banana', 'kiwi', 'apple']
# Fruits = input('enter a fruits name')
if 'mango' in Fruits:
    print('yes this fruits is in list')
else:
    print('no this fruits is in list ')    



# 													some more list method   
# count 
# sort method
# sorted method
# reverse 
# clear
# copy 
Fruits = ['orange', 'pear', 'banana', 'kiwi', 'apple', 'orange','kiwi','apple']
# count method 
print(Fruits.count('apple'))
# sort method
number = [2,4,5,6,7,8,8,9,3,4,1] # we can also use alphabate and number
number.sort()
print(number)
# sorted method
number = [2,4,5,6,7,8,8,9,3,4,1]
print(sorted(number))
# clear
number = [2,4,5,6,7,8,8,9,3,4,1]
number.clear()
print(number)
# copy
number = [2,4,5,6,7,8,8,9,3,4,1]
number_copy = number.copy()
print(number)
#  reverse
Fruits = ['orange', 'pear', 'banana', 'kiwi', 'apple', 'orange','kiwi','apple']
Fruits.reverse()
print(Fruits)

# 											'is' vs '=' comparison
# list comparison
Fruits1 = ['orange', 'pear', 'banana']
Fruits2 = ['orange', 'pear', 'banana']
print(Fruits1 == Fruits2)
print(Fruits1 is Fruits2)
Fruits2 = ['kiwi', 'apple', 'orange','kiwi','apple']
print(Fruits1 == Fruits2)


# 										join and sprit method
# split method
# convert split into list
name, age = input('enter your and age') .split(',')
print(name)
print(age)
name, age = 'Block_cipher,13' .split(',')
print(name)
print(age)
 
# join method 
# conver list into string
user_info = ['ram', '23']
print(','.join(user_info))

# 													list vs array

#  c , c++ , java
#  array int, string

# List - store any data / flexible

# python arrau madule - fixt data type

# numpy arrays - binding with c libraries

# javascript array = python list / flexible

# 												list vs string

# string are immutable
# Lists are mutable

G = 'mango' 
H = G.title()
print(H)

S = ['word1', 'word2', 'word3']
S.append('Gaurav')
print(S)

# 													looping in list 			
fruits = ['mango', 'banana', 'kiwi', 'orange', 'apple']
for i in fruits:
    print(i)

# while loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1


# 															list inside list
matrix = [[1,2,3,4,5],[5,6,7,8,9],[5,6,4,2,5,5]] # 2d list 
for i in matrix:
    print(i)
# 
for name in matrix:
    for i in name:
        print(i)  

matrix = [[1,2,3,4,5],[5,6,7,8,9],[5,6,4,2,5,5]]
print(matrix[2][5])        

# 						 Type function
H = 'gfaiejgoe'
print(type(H))
print(type(matrix))
num = (2,2,2,4,6,745)
print(type(num)) 

# 																	more about list 
# generate list with range function
# something more about pop method 
# index method
# pass list a function

#   generate list with range function 
numbers = list(range(1,11))
print(numbers)
# something more about pop method
numbers = list(range(1,11))
numbers.pop()
print(numbers)
# index method
#   = list(range(1,34))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 4, 5, 5, 5, 4, 4, 8, 9]
print(numbers.index(9, 4, 14))
# pass list to a function 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1,]
def numbers_0 (l):
    numbers = []
    for i in l:
        numbers.append(-i)
    return numbers
print(numbers_0(numbers))        


#                                                                   exercise of ch 5 
# print the sum of the sqare

numbers = list(range(1,89))
def square_list(l):
    square = []
    for i in l:
        square.append(i**2)
    return square
print(square_list(numbers))  

# second exercise of ch 5 
# define a function which will take list as a argument and this function 
# will return a reversed list 

# # examples
# [1,2,3,4,5] ----> [5,4,3,2,1]

# Note you simply do this with reverse or [::-1]

# but try to do this with the help of append or return method
def reverse_list(l):
    l.reverse()
    return l
numbers = list(range(1,100))
# numbers.reverse()
# print(numbers)
print(reverse_list(numbers))


# use of this [::-1]
def reverse_list(l):
    return l[::-1]
num = [1,2,3,4,5,6,7,8,9]  
print(reverse_list(num))  

# num = list(range(1,100))
num = [1,2,3,4,5,6]
def reverse_list(l):
    # l.append(l)
    return l[::-1]
    for i in l:
        reversed.pop(l)
    return reversed
print(reverse_list(num))        

#                                                                                third exercise of ch 5
# define a function that take list of words as argument
# return list with reverse of every element in that list 

# example 
# ['abc', 'bca','nca']


def reverse_elements(l):
    elements = []
    for i in l:
        elements.append(i[::-1])
    return elements 
word = ['abc','can','ban']
print(reverse_elements(word))   
 
#                                                                              4 exercise ch 5 
# filter odd even
# define a function 
# input 
# list ---> [1,2,3,4,5,6,7,8]

# output [1,3,5,7] [2,4,6,8]]

def filter_odd_even(l):
    odd_num = []
    even_num = []
    for i in l:
        if i % 2 == 0:
            even_num.append(i)
        else:
            odd_num.append(i)
    output = [even_num,odd_num]
    return output
num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]    
print(filter_odd_even(num))

#                                                                           exercise 5 ch 5
# common elements finder function 
# define a function which take 2 list as input and return a list 
# which contains common element of both lis t

# example 
# input ---> [1,2,5,8], [1,2,7,6]
# output ---> [1,2]

# num = [1,2,5,6],[3,4,5,6]

def commun_num(l1,l2):
    output = []
    # second_list = []
    for i in l1:
        if i in l2:
            output.append(i)

    return output
print(commun_num([1,2,5,6,4,8],[3,4,5,6,4,8]))                
#                                                                   min and max function
numbers = [1,2,3,4,56,64,6,]
# print(max(numbers))
# print(min(numbers))

def greatest_difference(l):
    return max(l) - min(l)
print(greatest_difference(numbers))    
    

#                                                                       last exercise
# function
# mixed = [1,2,3,4[1,2,3][1,2,4,5,6]]
# output
def sublist_counter(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
    return count
mixed = [1,2,3,4, [1,2,3], [2,3,7,5]]

print(sublist_counter(mixed))

        

        
















































    