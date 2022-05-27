# dictionary comprehension
square = {f'cube of {num} is':num**2 for num in range(1,11)}
for i,h in square.items():
    print(f'{i} : {h}')

string = "Gaurav"
word_count = {char:string.count(char) for char in string}
print(word_count)



# dictionary comprehension with if else statement
# d = {1:'odd', 2:'even'}
odd_even = {i:('even' if i%2 == 0 else 'odd')for i in range(1,11)}
print(odd_even)


# set comprehension 
s = {i**2 for i in range(1,11)}
print(s)

names = ['harshit','Block','mohit']
first = {i[0] for i in names}
print(first)



