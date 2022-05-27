# ***************************************************************************************************************************************************************************
# **************************************************************CH-6************************************************************************************************************
# ***************************************************************************************************************************************************************************
# ***************************************************************************************************************************************************************************
# ***************************************************************************************************************************************************************************
# ***************************************************************************************************************************************************************************
# ***************************************************************************************************************************************************************************




# tuple data structure
# tuple can store any data type 
# most important tuple are immutable, once tuple is created you can't update 
# data inside tuple 

example = ("one", "two", "three")
# no append, no inseret, no pop, no remove
# days = ("monday", "tuesday")
# tuple are then list


# method
# count, index 
# len function
# sliceing
print(example[:2])

# 											More about tuple
# looping in tuple
# tuple with one element
# tuple without parenthesis 
# tuple unpacking 
# list inside tuple
# sum function that you can use with tuple


mixed = (1,2,3,4.4)

# for loop and tuple
for i in mixed:
    print(i)

# note - you can use while loop with too


# tuple with one element
num = (1,)
word =('word')
print(type(word))
print(type(num))

# tuple without parenthesis 
guitars = 'yameha', 'baton rough', 'taylor'
print(type(guitars))


# tuple unpacking 
guitarists = ('ram', 'Bolck_cipher','fhsdj')
guitarists1,guitarists2,guitarists3 = (guitarists)
print(guitarists)

# list inside tuple
fovroties = ('southern hemesphere',['nothere hemespere', 'tropical evergreen foreset'])
fovroties[1].pop()
fovroties[1].append('we are very happy')
print(fovroties)

# sum function that you can use with tuple
# min(), max(),sum()
print(min(mixed))
print(max(mixed))
print(sum(mixed))

#                               function returning two value
def fun(int1,int2,):
    # subtract = int1-int2
    # divide = int1/int2
    add = int1+int2
    multiply = int1*int2
    return add,multiply#subtract,divide

add,multiply = fun(2,3)    
print(add)
print(multiply)
# print(divide)
# print(subtract)

#                                               some about tuple, list , string
num = tuple(range(1,11))
# num.range()
print(num)

num = list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(num)
num = str([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(type(num))