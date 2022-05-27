# *********************************************************************************************************************************************************
# ***************************************************************CH - 13***************************************************************************************
# *********************************************************************************************************************************************************
# *********************************************************************************************************************************************************


# ========================================================= enumerate() function ====================================================
# we use enumerate function with for loop to track position of our 
# item in iterrable



# How we can do this without enumerate function
names = ["abc", 'abcdef','Gaurav']
pos = 0
for i in names:
    print(f'{pos} -----> {i}')
    pos += 1

# with enumerate function

for pos,i in enumerate(names):
    print(f'{pos} ----> {i}')
        

# define a function that take two argument
# 1). list consting string
# 2). string that went to find in your list
# and this function will return the index of string in your list and 
# if string is not present then return -1


def func(l,target):
    for pos,name in enumerate(l):
        if name == target:
            return pos
    return -1  
print(func(names,'Gaurav'))    




#                                                               Map() function

number = [1,2,3,4]

def square(a):
    return a**2


squares = list(map(lambda a : a**2,number))    
print(squares)

# list comprehension
squares2 = [i**2 for i in number]
print(squares2)


new_list = []
for num in number:
    new_list.append(square(num))
print(new_list)

# NOTE 
# In map we cannot use more then on loop
# when we use map in list then we can use loop

name = ['abc','abcd','abcde']
length = list(map(len, name)) 
print(length)
for i in length:
    print(i)



#                                                                           filter() function 
# def is_even(a):
#     return a%2 == 0

number = [1,2,3,4,5,5,6,7,85,5,2,4,7,8,10,13,12]

evens = list(filter(lambda a:a%2 == 0 , number))
print(evens)
for i in evens:
    print(i)


evens2 = [i for i in number if i%2 == 0]
print(evens2)




#                                                                           iterator vs interable

# interable

number = [1,2,3,4] # tuple, string, -- iterables
squares = map(lambda a:a**2 ,number)

# for i in number:
#     print(i)

# numbers_item = iter(number)
# print(next(numbers_item))
# print(next(numbers_item))
# print(next(numbers_item))
# print(next(numbers_item))


# zip() function
user_id = ['user1','user2','user3']
name = ['ram','mohan','Gaurav']
last_name = ['kumar','kumar','kumar']

names = list(zip(user_id,name,last_name)) # we can also use dict function also 
print(names)

# example = [('a',1),('b',2)]
# print(dict(example))

# zip() function part 2
# l1 = [1,3,5,7]
# l2 = [2,4,6,8]

l = [(1,2),(3,4),(5,6),(7,8)]

l1,l2 = list(zip(*l))
print(list(l1))
print(list(l2))

l1 = [1,3,5,7]
l2 = [2,4,6,8]

new_list = []
for pair in zip(l1,l2):
    new_list.append(max(pair))
print(new_list)

# Advance function practice1
# THIS IS CHALLENGE

# define a function take any no of list containing number
# [1,2,3],[4,5,6],[7,8,9]
# return avarage
# (1+4+7)/3 , (2+5+8)/3 , (3+6+9)/3


# try to make this anonymous function in one line using lambda 
def avarage_finder(*args):
    avarage = []
    for pair in zip(*args):
        avarage.append(sum(pair)/len(pair))
    return avarage    
print(avarage_finder([1,2,3],[4,5,6],[7,8,9]))    


avarage_finder2 = lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]
print(avarage_finder([1,2,3],[4,5,6],[7,8,9]))



#                                                                           any() and all() function
number1 = [2,4,6,8,10]
number2 = [1,3,5,4,9]

even1= []
for num in number1:
    even1.append(num%2 == 0)
print(even1)        

# all function 
print(all([True, True, True,True,True]))

# list comprehension
print(all([num%2 == 0 for num in number1]))

# any function
number1 = [2,4,6,7,10]
number2 = [1,3,5,4,9]
print(any([num%2 == 0 for num in number2]))


# any() and all() function practice
def my_sum(*args):
    # args = ()
    if all([(type(arg) == int or type(arg) == float)for arg in args]):
        total = 0
        for num in args:
            total += num 
        return total    
    else:
        return 'wrong input !'    

print(my_sum(1,2,3,4,4.5,'worng input'  ))    



# Advance min() and max() function


# number = [1,2,3,4,5,6,7]
# print(min(number))

# def func(item):
#     return len(item)

name = ['Gaurav kumar','Block','ram','a','abc']
print(max(name , key = lambda item : len(item)))




students2 = [
    {'name' : 'amit', 'score' : 95 , 'age': 20},
    {'name' : 'harshit', 'score': 100, 'age' : 24},
    {'name' : 'Gaurav', 'score' : 200, 'age': 23}
]

print(max(students2 , key = lambda item:item.get('score'))['name'])


students = {
    'Gaurav' : {'score' : 90 , 'age': 13},
    'mohit' : {'score': 75, 'age' : 19},
    'ram' : {'score' : 85, 'age': 24}
}

print(max(students , key = lambda item:students[item]['age']))


#                                                                               Advance sorted() function

fruits = ['mango','grapes','apple']

# sort 
fruits.sort()
print(fruits)

Fruits2 = ('mango','grapes','apple')
print(sorted(fruits))

Fruits3 = {'mango','grapes','apple'}
print(sorted(Fruits3))


guitars = [
    {'model': 'yamaha f310', 'price':8400},
    {'model': 'faith naptune', 'price':50000},
    {'model': 'faith apollo venus', 'price': 35000},
    {'model': 'taylor 814ce', 'price': 450000}
]
print(sorted(guitars, key = lambda d:d['price']))pyt
# print(sorted(guitars, key = lambda d:d['price'], reverse = True ))


# Advance sorted() function
fruits = ['mango','grapes','apple']

# sort 
fruits.sort()
print(fruits)

Fruits2 = ('mango','grapes','apple')
print(sorted(fruits))

Fruits3 = {'mango','grapes','apple'}
print(sorted(Fruits3))


guitars = [
    {'model': 'yamaha f310', 'price':8400},
    {'model': 'faith naptune', 'price':50000},
    {'model': 'faith apollo venus', 'price': 35000},
    {'model': 'taylor 814ce', 'price': 450000}
]
print(sorted(guitars, key = lambda d:d['price']))
# print(sorted(guitars, key = lambda d:d['price'], reverse = True ))

#                                                       more about function
# what are doct string 
# how to write doctstring 
# how to see doctstring
# what is help function

def add(a,b):
    ''' this function take to number and return their sum '''
    return a+b
print(add(2,3))
print(add.__doc__)

# we learnt
# len, sum, max, min, sorted
# print(len.__doc__)
# print(sum.__doc__)
# print(len.__doc__)
# print(min.__doc__)
# print(sorted.__doc__)
# print(map.__doc__)

# help method
print(help(filter))























