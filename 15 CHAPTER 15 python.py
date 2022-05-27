# **************************************************************************************************************************************************************
# *********************************************************CH - 15*************************************************************************************************
# **************************************************************************************************************************************************************
# **************************************************************************************************************************************************************
# **************************************************************************************************************************************************************


# ========================================================= Intro to Generators ======================================================
# generators are iterator

# iterator , iterable


l = [1,2,3]  # iterable

# for i in l:
#     print(i)

# i = iter(l)
# print(next(i))
# print(next(i))
# print(next(i))
# # print(next(i))

# for i in map(lambda a:a**2, l):
#     print(i)

# l = [1,4,9,16]
# memory ---- [..................................................]
# memory ---- (..................................................)


# write first generators
# creat your first generators with Generator function
# this is my first project with genetator function 
# 1.) Generator function
# 2.) Generator comprehension

# 10 , 1 to 10

def nums(n):
    for i in range(1,n+1):
        yield i
# print(nums(10))  
for numbers in nums(10):
    # print(numbers)
# numbers = list(nums(10))
# for num in numbers:
#     print(num)

# for num in numbers:
#     print(num)    


#                                                                   ch 15 exercise 
# define generators function
# take one num as argument
# Generate a sequence of even num from 1 to that number

def even_generator(n):
    for i in range(1,n+1):
        if i%2 == 0:
            yield(i)
for num in even_generator(20):
    print(num)

# for num in even_generator(20):
#     print(num)

# for number in even_generator(8):
#     print(number)

def even_geneator(n):
    for i in range(2,n+1,2):
        yield(i)

        
for num in even_geneator(20):
    print(num) 


#                                                                       Generator comprehension
square_list = (i**2 for i in range(1,11))
print(list(square_list))
print(next(square_list))



#   
import time                                                                            list vs generators
# memory used, Time
# when to use list, when to use generators

# t1 = time.time()
# l = [i**2 for i in range(10000000)]
# print(time.time() - t1)
# print(t2-t1)
t1 = time.time()
l = (i**2 for i in range(10000000))
print(time.time() - t1)    