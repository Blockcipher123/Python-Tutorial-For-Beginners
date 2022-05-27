# ...................................................CHAPTER 4................................................................
# ****************************************************************************************************************************
# ****************************************************************************************************************************
# ***************************************************************************************************************************
# ***************************************************************************************************************************
# **********************************************************************************************************************


# .......................................Functions.........................................................................
def add_two(a,b):
    return a+b


num1 = int(input('enter first num'))
num2 = int(input('enter second num'))
total = add_two(num1,num2)
print (total)

first_name = input("enter first name")
last_name = input("enter last name")
total = add_two(first_name,last_name)
print(total)

# ....................................................print vs return.......................................................
def add_three(a,b,c):
	return(a+b+c)
	
print(add_three(3,4,6))

def add_three(a,b,c):
	print(a+b+c)

add_three(2,3,4)


def add_four(a,b,c,d):
	return(a+b+c+d)

add_four(3,4,2,5)


#                                           function practice
def last_char(name):
    return name[-1]

print(last_char('Gaurav'))    
#                                              odd and even
def odd_even(num):
    if num%2 == 0:
        return 'even'
    else:
        return 'odd'    

print(odd_even(826482))   

def odd_even(num):
    if num%2 == 0:
        return 'even'
    return 'odd'    
    
print(odd_even(826482))   


#                                               is even
def is_even(num):
    if num%2 == 0:
        return True
    return False    

print(is_even(5))  


def is_even(num):
    return num%2 == 0

print(is_even(5))     

def movie():
    return 'Avnger End Game'
print(movie())    

# ..........................................ecercise CH 4................................................
# we can input two num by using fun
def two_num(a,b):
    if a>b:
        return a
    else:
        return  b
print(two_num(6,11))    

#                                                 user taken
def greater(a,b): 
    if a>b:
        return a 
    else:
        return  b
    
num1 = int(input('enter first num'))
num2 = int(input('enter second num'))
biggner = greater(num1,num2)
print(f"{biggner} is greater")    


# ..........................................we can input three num by using fun.......................................
# ...........................................Define function..............................................................
def greatest(a,b,c): 
    if a>b and a>c:
        return a 
    elif b>a and b>c:
        return b
    else:
        return  c        
num1 = int(input('enter first num'))
num2 = int(input('enter second num'))
num3 = int(input('enter third num'))
biggner = greatest(num1,num2,num3)
print(f"{biggner} is greatest")    


#                                   we can input three num by using function

def greatest(a,b,c): 
    if a>b and a>c:
        return a 
    elif b>a and b>c:
        return b
    else:
        return  c    

print(greatest(23,56,67))


# ...............................function_inside_function.........................................
def new_greatest(a,b,c):
    bigger = greater(a,b)
    return greater(bigger, c)

print(new_greatest(123,232,4352))    

# kiss -- keep it simple stupid 

def new_greatest(a,b,c):
    bigger = greater(a,b)
    return greater(greater(a,b), c)

print(new_greatest(123,232,4352)

# .................................execise 2 CH 4.............................................................
def is_palindrome(name):
    reversed_name = name[::-1]
    if name == reversed_name:
        return True
    else:
        return False  
    # if name[::-1]:

# mytext = is_palindrome(name)
# name = input('enter your name')

# print(mytext)
def is_palindrome(name):
    return name == name[::-1]


print(is_palindrome('naman'))
print(is_palindrome('Gaurav'))

#                                       Define_fibonacci_series
# 0 1 1 2 3 5 8 13 21 34

# 1 ---> 1  
# 2 ---> 0 1 
# 3 ---> 0 1 1

# for i in range(1,101):
    # print(i, end = ",")


def fibonacci_seq(n):
    a = 0 # first num
    b = 1 # second num
    if n == 1:
        print(a)
    elif n == 2:
        print(a, b)
    else:
        print(a,b, end = " ")
        for i in range(n-2):
            c = a + b # c = 1
            a = b # a = 1 
            b = c # b = 1
            print(b, end = " ")

fibonacci_seq(100)          

# ....................................Default Parameters.....................................................
def user_info(first_name, second_name, age):
    print(f"your first name is {first_name}")
    print(f"your second name is {second_name}")
    print(f"your age is {age}")


user_info('Block', 'Cipher',13)   



def user_info(first_name = "unknown", second_name = "unknown", age = None):
    print(f"your first name is {first_name}")
    print(f"your second name is {second_name}")
    print(f"your age is {age}")


user_info()   

# ................scope of veriable inside and outside function...........................
# Scope
x = 5 # Global veriable 


def func():
    global x 
    x = 15 # local veriable
    return x

print(x) 
print(func())
print(x)    
