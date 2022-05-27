# *********************************************************************************************************************************************************
# *********************************************************************************************************************************************************
# *****************************************************CH - 20*********************************************************************************************
# *********************************************************************************************************************************************************
# *********************************************************************************************************************************************************
# *********************************************************************************************************************************************************



# CH - 20
# ============================================================== os module ============================================================
import os

#  os.getcwd()
# print(os.getcwd())


# for creating floder
# os.mkdir('python')
# os.mkdir('programer')
# how can we a folder is already exist or not
# # print(os.path.exists('programer'))
# if os.path.exists('pragramer'):
#     print('already exist')
# else:
#     os.mkdir('programer')    


# How to creat file 
# open('file9.html','a').close()

# how to creat folder in new disk
# os.mkdir(r'E:\Default\Photoss.html')

# this method make a list of file in the folder
# print(os.listdir())

# creat make a list of file in the folder in new disk
# print(os.listdir(r'E:\Default'))

# for creat a path of a file or folder

# for item in os.listdir(): # we don't use more
#     print(r'F:\python' + '\\' + item)

# for item in os.listdir('E:\Default'): # we use more 
#     path = os.path.join(r'E:\Default',item)
#     print(path)


#                                           os & shutil module

# this is for how creat a path folder inside floder
import os 
# os.chdir(r'F:\python')
# # print(os.listdir())

# fileiter = os.walk(r'F:\python')
# for current_path, floder_name, file_name in fileiter:
#     print(f'current path : {current_path}')
#     print(f'floder name : {floder_name}')
#     print(f'file name : {file_name}')


# Delete folder, file
# os.rmdir('programer')
# delete mtfolder

# creat folder inside folder in one step
# os.makedirs('programer/new/python')

# delete folder prmentley
# shutil.rmtree('programer')

# copy folder 
# shutil.copytree('world','programer/world')
# shutil.copy('file1.txt','programer/file1.txt')

# move any file or folder
# shutil.move('file1.txt','programer/file2.txt')
shutil.move('world','programer/world')