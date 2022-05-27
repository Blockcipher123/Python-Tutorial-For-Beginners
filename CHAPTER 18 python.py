# ****************************************************************************************************************************************
# ************************************************CH - 18************************************************************************************
# ****************************************************************************************************************************************
# ****************************************************************************************************************************************
# ****************************************************************************************************************************************



# =================================================== Read text file =============================================================
# read file
# open function
# read method
# seek method
# tell method
# readline method
# readlines method
# close method


f = open(r"F:\Block_cipher\Text\Hacker rank.txt")
# name, closed
# print(f.name)
# print(f.closed)
for i in f.readlines()[:4]:
    print(i, end='')

f.close()




# print(f'cursor position --> {f.tell()}')
# print(f.read())
# print(f.readline(), end= '')
# print(f.readline(), end= "")
# print(f.readline(), end= "")
# print(f'cursor position --> {f.tell()}')
# print('befor seek method')
# f.seek(0)
# print('after seek method ')
# print(f'cursor position --> {f.tell()}')
# print(f.read())
# line = f.readlines()
# # print(len(line))
# for i in line:
#     print(i, end= '')


# 																With blocks
# we can use this for many thing
# with block
# context manager

with open('reading file .txt') as f :
    data = f.read()
    print(data)

print(f.closed)    

# write to file
# we can use this sort cut to write 
# w,a,r+
# w function
# with open('reading file .txt' , 'w') as g:
#     g.write('This is my best video in this chapter i learn programming  ') 
# a function
with open('file.txt' , 'r+') as g:
    g.seek(len(g.read()))
    g.write('This is my best vidong and please do it \n ') 



# 																	read and WRITE
with open('file.txt' , 'r') as rf:
    with open('file1.txt', 'w') as wf:
        wf.write(rf.read())

# 																	exercise of ch 17 

with open('file1.txt', 'r') as rf:
    with open('file.txt', 'a') as wf:
        for line in rf.readlines():
            name, salary = line.split(',')
            wf.write(f'{name}\'s, salary is {salary}')


# 																  exercise 2 ch 17

# with open("index.html", 'r') as webpage:
#     with open('file1.txt',  'a') as wf:
#         for i in webpage.readlines():
#             if '<a href=' in i:
#                 pos = i.find('<a href=')
#                 link = i.find('\"',pos) 
#                 link2 = i.find('\"',link+1)
#                 url = i[link+1:link2]
#                 wf.write(url + '\n')


with open("index.html", 'r') as webpage:
    with open('output.txt',  'a') as wf:
        page = webpage.read()
        link_exist = True
        while link_exist:
            pos = page.find('<a href=')
            if pos == -1:
                link_exist = False
            else:
                link = page.find('\"',pos) 
                link2 = page.find('\"',link+1)
                url = page[link+1:link2]
                wf.write(url + '\n')
                page = page[link2:]
