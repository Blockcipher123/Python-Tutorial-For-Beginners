# ************************************************************************************************************************************************
# *********************************************************CH - 14*************************************************************************************
# ************************************************************************************************************************************************
# ************************************************************************************************************************************************
# ************************************************************************************************************************************************



# ch 14 Introduction
# you have to have a compleat understanding of function
# first class function / closures 
# then finally well learnt about decoraters

def square(a):
    return a**2 

# print(sqare(7))    
s = square
# print(s(7))
print(s.__name__)
print(square.__name__)
print(s)
print(square)



# pass function as a argument
# map 
def square(a):
    return a**2

l = [1,2,3,4]
# print(list(map(lambda a:a**2,l)))

def my_map(func,l):
    new_list = []
    for item in l:
        new_list.append(func(item))
    return new_list
print(my_map(lambda a:a**3,l))        

def my_map2(fun,l):
    return [fun(item) for item in l]
print(my_map2(lambda a:a**3,l))     


# function returning function
def outer_func():
    def inner_func():
        print('inside inner func')
    return inner_func
var = outer_func()
var ()

def outer_func2(mag):
    def inner_func2():
        print(f"massage is {mag}")
    return inner_func2
var2 = outer_func2('hello there !')
var2()      


# closures practice
# function returning function (closures) practice
def to_power(x):
    def calc_power(n):
        return x**n
    return calc_power

cube = to_power(3)
print(cube(8))        

square = to_power(2)
print(square(4))

#                                                                                           decorators intro
# @ use for decorators
def decorators_function(any_function):
    def wrapper_function():
        print('this is awesome function ')
        any_function()
    return wrapper_function    

# this is awesome function
@decorators_function # this is shortcut
def func1():
    print('this is function 1')
func1()

# this is awesome function
@decorators_function
def func2():
    print('this is function 2')
func2()
# func1 = decorators_function(func1)
# func1()


# decorators part 2
def decorators_function(any_function):
    def wrapper_function(*args,**kwargs):
        print('this is awesome function ')
        return any_function(*args,**kwargs)
    return wrapper_function 

@decorators_function
def func(a):
    print(f'this is function with argument {a}')    
func(7)    

@decorators_function
def sums(a,b):
    return a + b
print(sums(2,3))    


# decorators part 3
from functools import wraps
def decorators_function(any_function):
    @wraps(any_function)
    def wrapper_function(*args,**kwargs):
        ''' this wrapper function '''
        print('this is awesome function ')
        return any_function(*args,**kwargs)
    return wrapper_function 

@decorators_function
def add(a,b):
    ''' this is add function '''
    return a + b
print(add(3,4))  
print(add.__doc__)
print(add.__name__)  



# decorators practice
from functools import wraps

def print_function_data(function):
    @wraps(function)
    def wrapper_function(*args , **kwargs):
        print(f'You calling {function.__name__} function')
        print(f"{function.__doc__}")
        return function(*args,**kwargs)
    return wrapper_function


@print_function_data
def add(a,b):
    ''' this function take two argument as argument and return their sum 😀😁😀👿👩👨'''
    return a + b

print(add(5,9))    
# output
# you are calling add function
# this function take two argument as argument and return their sum


#                                                                       exercise ch 14 

from functools import wraps
import time
def calculate_time(function):
    @wraps(function)
    def wrapper(*args , **kwargs):
        print(f'Excecuting .... {function.__name__}')
        t1 = time.time()
        returned_value = function(*args,**kwargs)
        t2 = time.time()
        total_time = t2 - t1
        print(f'this is function took {total_time} seconds to run')
        return returned_value
    return wrapper
 
@calculate_time
def square(a):
    return [i**2 for i in range(a,a+1)]
square(1000)


#                                                                               decorators practice2
# decorators practice2
from functools import wraps
def only_int_allow(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        data_types = []
        for arg in args:
            data_types.append(type(arg) == int)
        if all(data_types):
            return function(*args, **kwargs)    
        else:
            print('Invalid arguments')
    return wrapper

@only_int_allow
def add_all(*args):
    total = 0
    for i in args:
        total  += i
    return total
print(add_all(1,2,3,4,5,[1,2,3,4]))        

# with the help of list com
# decorators practice2
from functools import wraps
def only_int_allow(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        if all([type(arg) == int for arg in args]):
            return function(*args, **kwargs) 
        print('Invalid arguments')    
        # data_types = []
        # for arg in args:
        #     data_types.append(type(arg)==int)
        # if all(data_types):
        #     return function(*args, **kwargs)    
        # else:
        #     print('Invalid arguments')
    return wrapper

@only_int_allow
def add_all(*args):
    total = 0
    for i in args:
        total  += i
    return total
print(add_all(1,2,3,4,5,[6,6,7]))        
#                                                                               decorators with argument
from functools import wraps
def only_data_type_allow(data_type):
    def decorators(function):
        @wraps(function)
        def wrapper(*args,**kwargs):
            if all([type(arg) == data_type for arg in args]):
                return function(*args, **kwargs) 
            print('Invalid arguments') 
        return wrapper
    return decorators

@only_data_type_allow(str)
def string_join(*args):
    string = ''
    for i in args:
        string += i
    return string    
print(string_join('Gaurav', ' kumar', 'a'))   