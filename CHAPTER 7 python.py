# ***************************************************************************************************************************************************************************
# **************************************************************CH-7*************************************************************************************************************
# ***************************************************************************************************************************************************************************
# ***************************************************************************************************************************************************************************
# ***************************************************************************************************************************************************************************
# ***************************************************************************************************************************************************************************
# ***************************************************************************************************************************************************************************



# ======================================================= dictionaries intro ========================================================
# Q - why we use dectionaaries?
# A - Because of limitations of list 
# real data .


# Example
user = ['Gaurav',24, ['coco','ludo'],['gjfd','djhfd']]
# this list contains user name , age , fav movies , fav tunes
# you can do this but this is not a good way to do this.

 
# Q - what are dictionaries 
# A - unordered collections of data in key : value pair.


# how to create dictionaries
user = {'name': 'Gaurav', 'age': 24}
# print(user)
# print(type(user))


# second method to create dictionary
user1 = dict(name = 'Gaurav', age = 13)
# print(user1)
print(user1['name'])
print(user1['age'])

# how to access data from dictionary
# NOTe - There is no indexing because of unordered collections of data


# which type of data a dictionary can store?
# anything
# numbers, strings, list, dictionay

user_info = {
    'name' : 'Gaurav',
    'age' : 13,
    'fav_movie' : ['coco','ludo'],
    'fav_tunes' : ['gjfd','djhfd'],
}
print(user_info['fav_movie'])
# users = {
#     user1 : {
#         'name' : 'Gaurav',
#     'age' : 13,
#     'fav_movie' : ['coco','ludo'],
#     'fav_tunes' : ['gjfd','djhfd'],
#     }

# }
# print(users)

# How to add data to empty dictionary

user_info2 = {

}
user_info2['name'] = 'mohit'
user_info2['age'] = 13
print(user_info2)


#                                                                                   Looping & in keyword   

user1 = {
    'name' : 'Gaurav',
    'age' : 13,
    'fav_movie' : ['coco','ludo'],
    'fav_tunes' : ['gjfd','djhfd'],
    }

# check if key exist in dectionary
if 'fav_movie' in user1:
    print('present')    
else:
    print('not-present')    






#                                               check if value exist in dictionary -----> values method
if ['coco','ludo'] in user1.values():
    print('present')    
else:
    print('not-present') 




# loops in dictionries
# for i in user1:
#     print(i)

# values mehtod
user1_values = user1.values()
print(user1)
print(type(user1_values))

# key
user1_keys = user1.keys()
print(user1_keys)
print(type(user1_keys))

# loops in dectionaries
for i in user1:
    print(user1[i]) 

# items method
user_items = user1.items()
print(user_items)
print(type(user_items))

# items method usefull
for keys , values in user1.items():
    print(f"key is {keys} values is {values}")


# add & delete data from dictionaries

user_info = {
    'name' : 'Gaurav',
    'age' : 13,
    'fav_movie' : ['coco','ludo'],
    'fav_tunes' : ['gjfd','djhfd'],
    }


# how to add data 
# user_info['fav_lan'] = ['Chinese', 'English']
# print(user_info)


# pop method #Introduction at list one agoment we can pass
# popped_item = user_info.pop('fav_movie')
# print(f"popped item is {popped_item}")
# print(user_info)


# popitem method
popped_item = user_info.popitem()
print(user_info)
print(type(popped_item))    


#                                        add & delete data from dictionaries

user_info = {
    'name' : 'Gaurav',
    'age' : 13,
    'fav_movie' : ['coco','ludo'],
    'fav_tunes' : ['gjfd','djhfd'],
    }


# how to add data 
user_info['fav_lan'] = ['Chinese', 'English']
print(user_info)


# pop method #Introduction at list one agoment we can pass
popped_item = user_info.pop('fav_movie')
print(f"popped item is {popped_item}")
print(user_info)


# popitem method
popped_item = user_info.popitem()
print(user_info)
print(type(popped_item))




#                                                update function 



user_info = {
    'name' : 'Gaurav',
    'age' : 13,
    'fav_movie' : ['coco','ludo'],
    'fav_tunes' : ['gjfd','djhfd'],
    }

more_info = {
    'name' : 'Block_Cipher', 'state' : 'Bihar', 'hobbies' : ['programming','rading']
}

user_info.update(more_info)
print(user_info)


#                                                                   from key method
# f = {
#     'name' : 'unknown',
#     'age' : 'unknown',
# }
# print(f)

# f = dict.fromkeys(
#     ['name','age'],'unknown'
# )
# print(f)
    
#                                                                   get method

f = {
     'name' : 'Gaurav',
     'age' : 'unknown',
}
# print(f['name'])

print(f.get('names')) # better


# if 'name' in f:
#     print('present')
# else:
#     print('not present')

if f.get('names'):
    print('present')
else:
    print('not present')

# if none ---> false, else ---> true


#                                                   clear method
f = {
     'name' : 'Gaurav',
     'age' : 'unknown',
}

f.clear()
print(f)

#                                                                           copy method
f = {
     'name' : 'Gaurav',
     'age' : 'unknown',
}

f1 = f.copy()
# f1 = f 
# print(f1.popitem())
# print(f)


print(f1 is f)


# More about get method
# more about ger method, tow same keys in dectionaries 
user = {
    'name' : 'Gaurav',
    'age' : '13',
    'name' : 'Block',
}
print(user.get('names', 'not found'))



# # exercise 
def cube_finder(n):
    cubes = {
        
    }
    for i in range(1,n+1):
        cubes[i] = i**3
    return cubes
print(cube_finder(400000000))        



# word_counter exercise

def word_counter(string):
    count = {

    }
    for i in string:
        count[i] = string.count(i)
    return count
print(word_counter('gaurav'))     


# exercise of ch 7 
# user_info = {
#     'name' : 'Gaurav',
#     'age' : 13,
#     'fav_movie' : ['coco','ludo'],
#     'fav_tunes' : ['gjfd','djhfd'],
#     }


user = {

}

name = input('what is your name :')
age = input('whata is you age :')
fav_movie = input('what is you fav_movie  seperated by comma').split(",")
fav_song = input('what is you fav_song  seperated by comma').split(",")

user['name'] = name
user['age'] = age 
user['fav_movie'] = fav_movie
user['fav_song'] = fav_song
# print(user)

for key, value in user.items():
    print(f"{key} : {value}")


# word_counter exercise

def word_counter(string):
    count = {

    }
    for i in string:
        count[i] = string.count(i)
    return count
print(word_counter('gaurav'))     


# exercise of ch 7 
# user_info = {
#     'name' : 'Gaurav',
#     'age' : 13,
#     'fav_movie' : ['coco','ludo'],
#     'fav_tunes' : ['gjfd','djhfd'],
#     }


user = {

}

name = input('what is your name :')
age = input('whata is you age :')
fav_movie = input('what is you fav_movie  seperated by comma').split(",")
fav_song = input('what is you fav_song  seperated by comma').split(",")

user['name'] = name
user['age'] = age 
user['fav_movie'] = fav_movie
user['fav_song'] = fav_song
# print(user)

for key, value in user.items():
    print(f"{key} : {value}")    