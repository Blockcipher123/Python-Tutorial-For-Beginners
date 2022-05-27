# ************************************************************************************************************************************************************************
# **************************************************************CH - 9 ***************************************************************************************************
# ************************************************************************************************************************************************************************
# ************************************************************************************************************************************************************************
# ************************************************************************************************************************************************************************
# ************************************************************************************************************************************************************************

#    What is list comprehension ?
# with the help of list comprehension we can create of list in one line


# ========================================================== list comprehension ==============================================

# create a list of squares from 1 t0 10

squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares)    

squares2 = [i**2 for i in range(1,11)] 
print(squares2)


negative = [

]
for i in range(1,11):
    negative.append(-i)
print(negative)    

negative2 = [-i for i in range(1,11)]
print(negative2)


name = ['ram', 'mohit', 'harshit']
# print first word
new_word = []
for i in name:
    new_word.append(i[0])
print(new_word)    

new_list = [i[0] for i in name]
print(new_list) 



# exercise of ch 9

def reverse_string(l):
    element = []
    for i in l:
        element.append(i[::-1])
    return element
list_word = ['abc','cde','fgh']        
print(reverse_string(list_word))


# list comprition
list_word2 = [name[::-1] for name in list_word]
print(list_word2)

# list comprehension in with if statement
num = []
numbers = list(range(1,11))
for i in numbers:
    if i%2 == 0:
        num.append(i)
        
print(num)         

even_nums = [i for i in numbers if i%2 == 0]
print(even_nums)
odd_nums = [i for i in numbers if i%2 != 0]
print(odd_nums)


# exercise2 of ch 9

# def list_data_type(l):
#     inputs = []
#     for i in l:
#         if (type(i) == int or type(i) == float
#         inputs.type(str(i))
        
#     return inputs
# num = [True,False,[1,2,3,4],1,1.0,4]       
# print(list_data_type(num)) 


def list_data(l):
    return[str(i) for i in l if (type(i) == int or type(i) == float)]
print(list_data(num))    



# list comprehension with if-else statement
nums = [1,2,3,4,5,6,7,8,9,10]

new_list = []
for i in nums:
    if i%2 == 0:
        new_list.append(i*2)
    else:
        new_list.append(-i)
print(new_list)    

new_list2 = [i*2 if(i%2 == 0) else -i for i in nums]
print(new_list2)


# Nested list comprehension

# example = [[1,2,3], [1,2,3], [1,2,3]]


nested_comp = [[i for i in range(1,4)] for j in range (3)]
print(nested_comp)

new_list3 = []
for j in range(3):
    new_list3.append([1,2,3])
print(new_list3)    
























