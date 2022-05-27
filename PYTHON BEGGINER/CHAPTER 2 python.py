# ....................................................CH-2 OF PYTHON...............................................................
#**********************************************************************************************************************************
#**********************************************************************************************************************************
# ....................................................topics...........................................................................


# .....................................................input print................................................................
name = input("what is your name")
print("Hello" + name)
name = input("what your father name")
print("your father name is" + name)
name = input("what is your mother name")
print("your mother name is" + name)
name = input("you read in which class")
print("you read in class" + name)
age = input("what is your age")
print("your age is" + age)
name = input('what is your school name')
print('your school name is' + name)
name = input('which city you live')
print('you live in' + name)
name = input('what is your profession')      
print('your profession is' + name)
#.........................................................sting..........................................................
collection of chrector inside single quotes or dubble quate
first_name = "Gaurav "
last_name = "kumar"
full_name = first_name + last_name
print(full_name)
first_name = "Gaurav "
last_name = "kumar"
full_name = first_name + " " + last_name
print(full_name)
print(first_name + "3")
print(first_name + str(4))
print(first_name * 4)
user input
input function
name = input("type your name")
print("Hello" + name)
Books = input('type your Books name')
print("Her Book" + Books)
Books = input('type your Books name')
print("Book of " + Books)
name = input('type your name')
print('Hello' + name)
age = input("what is your age")
print("your age is" + age)
num = input('enter you num')
print('your num is' + num)
num1 = input('enter your num')
num2 = input('enter your num')
num3 = input('enter your num')
print(int(num1) +int(num2)+ int(num3))
num1 = input('enter your num')
num2 = input('enter your num')
print(int(num1) //int(num2))
# .........................................................string formiting............................................
string formiting are divided into three type
1. pyhton-2
2. python-3
3. python-3.6
# 
# 
#......................................................python 3........................................................
name = 'Gaurav'
age = 14
# 
print("Hello {} your age is  {} ".format(name, age))
print("Hello {} your age is  {} ".format(name, age+2))
#.......................................................PYTHON 3.6................................................
print(f"Hello {name} your age is {age-2}")
print(f"Hello {name} your age is {age}")
# ......................................................excercise ch 2.....................................................
# 
# 
# 
# 
num1 = input("enter your num")
num2 = input("enter your num")
num3 = input("enter your num")
# print((int(num1) + int(num2) + int(num3))//3)
print(f"average of three num : {(int(num1) + int(num2) + int(num3))//3}")





# 




# .............................................excercise of ch 2....................................................................
# 
# 
# 
# 
num1 = input('enter your num')
num2 = input('enter your num')
num3 = input('enter your num')
# print((int(num1) + int(num2) + int(num3)) //3)
print(f"average of three num : {((int(num1) + int(num2) + int(num3)) //3)}")

# # #...........................................................strint indexing..............................
#    # positions(index number)
   

# language = "python"   

#      # p = 0
#      # y = 1 
#      # t = 2
#      # h = 3
#      # o = 4
#      # n = 5       
print(language[0])     
print(language[1])
print(language[2])
print(language[3])
print(language[4])
print(language[5])
# 
# # #.....................................slicing / selecting sub sequences.......................................
name = "Block_cipher"
# syntax - (start argument : stop argument -1)

print(name[0:12])

subject = "math"
print(subject[0:5])

print(name[4:6])

print("Gaurav"[0:7])

# #      step argument  

print("laptop"[0:7:2])
print("laptop"[0:7:3])
print("laptop"[0::2])
print("laptop"[::-1])
print("laptop"[-1::-1])


# # string method part one (len function)

# # len function
name = 'Block_cipher'
print (len ('Block_cipher'))
# # 
# # name = 'Blockcipher'
length = len (name)
print(length)

# # # lower() method
# # # 
name = 'bLOck_CiPHeR'
print(name.lower())

# # upper() method
# # 
name = 'block_cipher56'
print(name.upper())

# # 
# # title() method
name = 'block_cipher'
print(name.title())

# # count() method
name = 'Block_cipher'
print(name.count("c"))

# ..........................................excercise 3....................................

# excercise
# Block_cipher
name = input('enter your name')
# print(f"single character" language[0])
language = 'code'
print(language[0])
print(len('name'))
print(name.count("h"))

# ....................solouation..............

name,char = input('enter comma seprated name and character : ').split(",")
print(f"length of your num is {len(name)}")
print(f"character count : {name.lower().count(char.lower())}") # case sensitive 
# 
# 
# ...........................................string_method..............................................
name = '      Gau     rav        '
docts = '.........'
# lstrip() method 
# print(name + docts)
print(name.lstrip() + docts)
print(name.rstrip() + docts)
print(name.strip() + docts)
print(name.replace(" ", "") + docts)


# ...........................................strip_method..............................................
name = '      Gau     rav        '
docts = '.........'
# lstrip() method 
# print(name + docts)
print(name.lstrip() + docts)
print(name.rstrip() + docts)
print(name.strip() + docts)
print(name.replace(" ", "") + docts)
a = int(input())
b = int(input())
print(int(a//b))
print(a/b)
    a = int(input())
    b = int(input())
    a = int(input())
    b = int(input())
number = '12345'
# n = int(input())
# print(int())
print(number[3])
n = int(input())
# 
# 
# 
# ...................................replace and find method...............................................
# replace () method
# find () method

# ........replace method...........
string = 'she is a very beautiful and she is a dancer'
print(string.replace(' ', '_'))
sentence = 'ram is a bad boy and shayam is a good boy'
print(sentence.replace("a", " ",4))
# ....make programs.........
name = input('enter your name')
print(name.center(len(name)+8,'*'))
name = input('enter your age')
print(name.center(len(name)+4, '😊'))
name = input('enter your hobby')
print(name.center(len(name)+6, '🍔'))
name = input('write the father of computer')
print(name.center(len(name)+10, '💻'))
name = input('who was the chief minester of bihar')
print(name.center(len(name)+4, '👴'))
name = input('who was the prime minester of india')
print(name.center(len(name)+6, '🧓')) 
name = input('write 5 animal name')
print(name.center(len(name)+8, '🐆'))
name = input('write 5 flower name')
print(name.center(len(name)+6, '🌷'))
name = input('define computer')
print(name.center(len(name)+16, '🖥'))
name = input('write two input divise')
print(name.center(len(name)+8, '⏳'))
name = input('write two output name')
print(name.center(len(name)+12, '⏳'))
name = input('enter your name')
print('well done' + name)
# 
# .......find method......
name = 'ramesh is a speak english and shayam does not speak english'
print(name.find('speak', 1))

#  see this  ---------->
name1 = 'their are 13 num of boys and 10 num of girls'
is_pos1 = name1.find('of', 1) # is pos1 ------->number
is_pos2 = name1.find('of', is_pos1 + 1)
print(is_pos2)



# .................................center method with program................................................
# center () method 
name = 'Block_cipher'
#  **Block_cipher 
print(name.center(16, '*'))


name = input('enter your name : ')
print(name.center(len(name)+8 , '*'))


# ..........................................string are immutable...............................................
string = 'supriya'
# print(string.replace('s', 'S'))
# string[3] 'R' # you cannot change the small r into capital R
print(string.replace('r', 'R'))
print(string)
     
     # python = immutable
     # rubi = mutable


# ............................................more assignment operator...............................................
num = '2'
num = num + ",3" 
print(num)
# 
name = 'Apple'
name += 'ka file'
print(name)
# 
age = 23
age = age + 1  
print(age)

age = 4
age *= 3    # (we can use this method we can also find +,-,*,/)
print(age)

# ....................................CHAPTER 2 SUMMARY(REVISION)...................................................
# NOTING
