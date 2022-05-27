# ***************************************************************************************************************************************************************
# ***************************************************************************************************************************************************************
# **************************************************************CH - 17*********************************************************************************************
# ***************************************************************************************************************************************************************
# ***************************************************************************************************************************************************************
# ***************************************************************************************************************************************************************


# ========================================================== Error Handling ========================================================
# intro to chapter 17 builts in error
# buits in errors
# Exception , how to handle them
# raise you own error, dubugging, etc 



# SyntaxError 

# def fun:
#     pass
# name = 'agj'*


# raise error
# NotImplementedError
# abstract method

def add(a,b):
    if (type(a) is int) and (type(b) is int):
        return a+b
    raise TypeError ('OOPs you are passing wron input in this function')    


print(add('3','3'))    

raise error example 1
NotImplementedError 
abstract method

class Animal:
    def __init__(self, name):
        self.name = name

        
    # abstract method    
    def sound(self):
        raise NotImplementedError('you have to define this in subclass ')    


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)    
        self.breed = breed
    def sound(self):
        return 'bhow-bhow'


class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return 'meow-meow'



# doggy = Dog('boony' , 'pug', )
# print(doggy.sound())



#                                                               raise example 2
class Mobile:
    def __init__(self, name):
        self.name = name


class MobileStore:
    def __init__(self):
        self.Mobiles = []        


    def add(self,new_mobile):
        if isinstance(new_mobile, Mobile):
            self.Mobiles.append(new_mobile) 
        else:
            raise TypeError('new mobile should be object of Mobile class')    
           


onePlus = Mobile('onePlus 6')        
samsung = 'samsung galaxt s21'


mobostore = MobileStore()
# print(mobostore.Mobiles)
print(mobostore.add(onePlus))
mobo_phone = mobostore.Mobiles
print(mobo_phone[0].name )



#                                                               hand exceptions
# Exception handing
# try except else finally



while True:
    try:
        age = int(input('enter you age : '))
        break

    except ValueError:
        print('Invalid input...')

    except:
        print('unexpected error ...')    



if age > 18:
    print('you can play this game')
else:
    raise TypeError('you can\'t play this game')


#                                                           else and finally clause in Exception handing


while True:
    try:
        number = int(input('enter a number : '))

    except ValueError:
        print('please enter integer !!')
    except:
        print('unexpected error !!!')    
    else:
        print(f'use input {number}')
        break
    finally:
        print('finally blocks .....')        


#                                                               exercise ch 17 
#     number = int(input('enter a number'))
def divide (a,b):
    try:
        return a/b
    except ZeroDivisionError as error:
        # print('you cannot divide a number by zero !! 😓😓 ')
        print(error)
    except TypeError as error:
        print(error)
        # print('you cannot divide a number by string !! 😓😓')
    except:
        print('unexpeted error !!')    
print(divide(4,'2'))


    
#                                                   custom exceptions
# python custom exceptions
# Q - why custom exceptions?
# A - To increase  the readbility of code.

# example\
class NameTooShortError(ValueError):
    pass

def validate(name):
    if len(name) < 8:
        raise NameTooShortError('name is to short')


username = input('Enter you name')
validate(username)
print(f'hello{username}')


#                                                           dubugging
# import pdb # import pdb module 
# module = python file contains usefull classes and functions were wrote 
# by developer


# According to wikipedia - Dubugging is the process of finding resolving defects or problem within problems within a computer program that prevent correct oparation of computer software or a system.

# why dubugging
# 1.) our program is not running and causing unexpected errors.
# 2.) our program is working fine but not working the same way we want



# steps for dubugging
# 1.) set trace 
# 2.) execute code line by line

pdb.set_trace
name = input('enter your name')
age = int(input('enter your age'))
print(f'hello {name} your age is {age}')
age2 = age + 5
print(f'hello{name} you will be {age2} in next five year')

# l
# c
# q












