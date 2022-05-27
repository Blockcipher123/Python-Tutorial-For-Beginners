# ...................................................CHAPTER 3 .....................................................
# ***************************************************************************************************************
# ***************************************************************************************************************
# ***************************************************************************************************************
# ***************************************************************************************************************
# ............................................if statement..........................................................
age = input("enter your age")
age = int(age)
if age >= 18:
	print('you can drive car')

# ...........................................pass statement.....................................................
x = 18 
if x >= 18:
	pass
# ............................................else statement....................................................
age = input("enter your age")
age = int(age)
if age >= 18:
	print('you can drive car')
else:  
	print("sorry, you can't drive a car")

# ........................................Excersice of guessing game...................................... 





# ........................................make a num guessing game....................................................
winning_num = 37
user_input = input('guess a num b/w 1 and 100')
user_input = int(user_input)
if user_input == winning_num:
	print('YOU WIN !!!')
else: # nested if else
    if user_input < winning_num:
      print('too low')
    else:
        print("too high")   


# ..........................................and , or operator....................................................................
# ANS FUN
name = 'abc'
age = 19
if name=='abc' and age==19:
    print("condition True")
else:
    print("codition False")    

 # OR FUN  
name = 'abc'
age = 19
if name=='abc' or age==18:
    print("condition True")
else:
    print("codition False")   
   
# .....................................................if_elif_else.........................................................................

# ..................................Film ticket.......................................................
#  age 0 to 3 (free ticket)
#  age 4 to 10 (150)
#  age 11 to 60 (250)
#  age above 60 (200)


age = input("enter your age")
age = int(age)

if age==0 or age < 0 :
    print("you can'n watch")

elif 1<age<=3:
    print("Ticket prise : Free") 
elif 3<age<=10:
    print("Ticket prise : 150")
elif 10<age<60:
    print("Ticket prise : 250")
else:
    print("Ticket prise : 200")
# ..............................................in keyword...............................................................
name = 'Block_cipher'
if "_" in name:
    print('YES present !!!')
else:
    print('NOT present !!!')

# ........................................................check_empty_or_not........................................................ 
name = input('enter your name')
if name:
    print('YES name is {empty} ')   
else:
    print("you don't type.....")


# .......................................TOPICE LOOP.........................................................
# ........................................While loop or for loop................................................
# print('Hello world'
g = 1 
while g<=10:
    print(f"Hello world {g}")
    g = g + 1   

# .................................pragame with while loop...................................................
total = 0
i = 1
while i <= 20:
    total += i 
    i += 1
print(total)

# ...............................excercise1 of ch 3........................................................
# excercise one of three
# sum of n natural numbers
# ask a user for a natural number(n) 
# print total from 1 to n 
# 
n = input('enter a number') 
n = int(n)
total = 0
i=1
while i <= n:
    total += i
    i+=1
print(total)    
        

# .............................................excercise 2.........................................................
# problem
# ask user to input a num containing more then one digit
# example --- 1256
# calculate 1+2+3+4+5
# 
# 
# 
# algorithm - (method to solve proglam in human language ) 
# ask input in string, i.e don't change string to int
# example = "1256"
# pick string chracter one by one and change to int
# int(example[0]) + int(example[1]) .... go up len(example) 
       

number = input("enter a num")
total = 0 
i = 0
while i < len(number):
    total += int(number[i])
    i += 1
print(total)            

# .................................excercise 3................................................... 
# ask a user for  name 
# example Block_cipher
# print count of each word
# output :
        # B : 1
        # l : 1
        # o : 1
        # c : 2
        # k : 1
        # _ : 1
        # c : 2
        # i : 1
        # p : 1
        # h : 1
        # e : 1
        # r : 1
  
name = input("enter your name     ")
temp_ver = "h"  
i = 0
while i < len(name):
    if name [i] not in temp_ver:
            temp_ver += name[i]
            print(f"{name[i]} : {name.count(name[i])}")
    i += 1 

# .............................infinite loop......................................
i = 0 
while i <= 10:
    print('Block_cipher')
    i += 1
# True
# Fale
while True:
    print('hello world')

# .................. programe with for_loop............................................
for i in range (1,11):
    print(f"amit {i}")
# 
for i in range (1,100):
    print('Block_cipher')
    
# ..................................for loop example1........................................................
# excercise one of three
# sum of n natural numbers
# ask a user for a natural number(n) 
# print total from 1 to n

num = int(input('enter  num'))
total = 0
i = 0
for i in range(1,num+1 ):
    total += i
print(total)    

# ...................................for_loop_example2...................................................
# problem
# ask user to input a num containing more then one digit
# example --- 1256
# calculate 1+2+3+4+5
# 
# 
# 
# algorithm - (method to solve proglam in human language ) 
# ask input in string, i.e don't change string to int
# example = "1256"
# pick string chracter one by one and change to int
# int(example[0]) + int(example[1]) .... go up len(example) 
       
num = input('')
total = 0
for i in range(0, len(num)):
    total += int(num[i])
print(total)        

# ...................................for_loop_example3...........................................
# ask a user for  name 
# example Block_cipher
# print count of each word
# output :
        # B : 1
        # l : 1
        # o : 1
        # c : 2
        # k : 1
        # _ : 1
        # c : 2
        # i : 1
        # p : 1
        # h : 1
        # e : 1
        # r : 1                

name = input('enter your name')
temp = ""
for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]}: {name.count(name[i])}")
        temp += name[i] 

# ..............................continue_and_brake_statement....................................................
# ....................................Brake statement...............................................
for i in range(1,11):
    if i == 5:
        break
    print(i)   

# ..........................................continue_statement............................................
for i in range(1,11):
    if i == 7:
        continue
    print(i)
        
# ........................................make a num guessing game....................................................
import random
winning_number = random.randint(1,100)
guess = 1
number = int(input('guess a num b/w 1 and 100'))
game_over = False


while not game_over:
    if number == winning_number:
            print(f"YOU WIN , and you guess this number in {guess} times ")
            game_over = True
    else:
        if number < winning_number:
            print('too low')
            guess += 1
            number = int(input("Sorry Guess again : "))
        else :
            print('too high')
            guess += 1      
            number = int(input("Sorry Guess again : "))                   

# ................................................DRY principle by make a num guessing game............................................
import random
winning_number = random.randint(1,100)
guess = 1
number = int(input('guess a num b/w 1 and 100'))
game_over = False


while not game_over:
    if number == winning_number:
            print(f"YOU WIN , and you guess this number in {guess} times ")
            game_over = True
    else:
        if number < winning_number:
            print('too low')
        else :
            print('too high')

        guess += 1      
        number = int(input("Sorry Guess again : "))

        
#  .....................................Stem argument in range function.............................................
for i in range(1,11,1):
    print(i)

for i in range(1, -11, -1):
    print(i)


# ..............................................................For loop and string.................................................
num = input('enter a num')
total = 0
for i in num:
    total += int(i)
print(total)    



name = 'Gaurav kumar'
for i in name:
    print(i)



   