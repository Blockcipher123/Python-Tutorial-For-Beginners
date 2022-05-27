# ***********************************************************************************************************************************************************************
# ***********************************************************************************************************************************************************************
# *********************************************************CH - 11*******************************************************************************************************
# ***********************************************************************************************************************************************************************
# ***********************************************************************************************************************************************************************
# ***********************************************************************************************************************************************************************


# Intro to * age
# make flexible function
# * operator
# * args

# def total(a,b,c,d):
#     return a+b+c+d


# def all_total(*args):
#     print(args)
#     print(type(args))
# all_total(1,2,3,4,42,4,232)    
 

def all_total(*args):
    # 1,2,3,4,42,4,232
    total = 0
    for num in args:
        total += num
    return total
print(all_total(1,2,3,4,42,4,232))        


# *args with normal parameters
def multiply_nums(num1,num2,*args):
    multiply = 1
    print(args)
    # print(num)
    for i in args:
        multiply *= i
    return multiply
print(multiply_nums(1,2,3,3))


# * args as a argument

def multiply_nums(*args):
    multiply = 1
    print(args) 2
    # print(num)
    for i in args:
        multiply *= i
    return multiply
num = [2,3,4]   
print(multiply_nums(*num)) # unpack
# print(type(num))
#                                               exercise of ch - 11
# defin a function
# input

# num, iterable(tuple,list)containing numbera as args

# example
# nums = [1,2,3]
# to power (3 *multiply_nums)

# output
# list ---> [1**3,8,27]

# if user didn't pass any args then give a user a massage 'hey you did't pass args

# else
# return list

# Note - use list comprehension 



# def cube_(num,*args):
#     # multiply = 1
#     # print(args)
#     # print(list)
#     # print(num)
#     for i in args:
#         if args:
#             return[i**num]
#         else:
#             return "you did't pass args"    
# nums = [1,2,3]        
# print(cube_(2,*nums))


def to_power(num, *args):
    if args:
        return [i**num for i in args]
    else:
        return "you didn't pass any args"

nums = [2,3,4]        
print(to_power(2,*[2,3]))        



# ** kwargs
# kwargs (keyword argument)
# ** kwargs (dubble star operator)

# kwargs as a perameter
def func(name,**kwargs):
    print(kwargs)
    print(type(kwargs))
    print(name)

    for k,e in kwargs.items():
        print(f'{k} : {e}')
func('mohit',first_name = 'Gaurav', last_name = 'Kumar')   


# dictionary unpacking 
d = {
    'name' : 'Block',
    'age' : 13,
    'class' : 8,
}
func(**d)






# function with all type a parameters
# very important to understand

# PADK


# parameters
# * args
# Default parameters
# ** kwargs


# Default parameters
def func(name = 'unknown' , age = 13):
    print(name)
    print(age)

func('GAURAV',14)

# all we use
def func(name,*args,last_name = 'unknown',**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

func('Gaurav',2,3,4,a = 1, b = 2)    


#                                                            exercise2 of ch 11

def func(l,**kwargs):
    if kwargs.get('reverse_str') == True:
        return [name[::-1].title() for name in l]
    else:
        return[name.title()for name in l]
names = ['gaurav','mohit']        
print(func(names,))         


# name = ['Gaurav','Mohi t']

# print(func(name ,reversed_str = True))
# def func(name) 


