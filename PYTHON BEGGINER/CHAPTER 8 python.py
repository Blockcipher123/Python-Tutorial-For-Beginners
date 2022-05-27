# set data type
# unordered collections of unique items

# s = {1,2,2,3,3,5,5,7,8,4,4,4,4,3,3,2,5,6,7,5,9,9,8,5}
# print(s)

l = [1,2,2,4,4,6,7,8,7,5,7,7,5,8]
# remove duplicate
s2 = list(set(l))
print(s2)
print(type(s2))

# set method
# Add
s = {1,2,3,4}
s.add(5)
s.add(6)
print(s)

# remove method
s = {1,2,3,4}
s.remove(3)
print(s)

# discard method
s = {1,2,3,4}
s.discard(5)
print(s)

# clear method
s = {1,2,3,4}
s.clear()
print(s)

# copy method
s = {1,2,3,4}
s1 = s.copy()
print(s1)

# we can store in like
s = {1,1.0,2.4,"string"}
print(s)


# more about set
# in Keyword in set and for Loop

s = {'a','b','c'}

if 'a' in s:
    print('present')
else:
    print('not present')   


# for loop
for item in s:
    print(item)

# set maths 
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

# two type of set 
# 1. union
# 2. intersection


# | union
union_set = s1 | s2
print(union_set)

# intersection
print(s1 & s2)


