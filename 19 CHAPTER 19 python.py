# ****************************************************************************************************************************************
# ****************************************************************************************************************************************
# ******************************************************CH - 19****************************************************************************
# ****************************************************************************************************************************************
# ****************************************************************************************************************************************
# ****************************************************************************************************************************************



# ========================================================= more_about_file ==========================================================
# with open('love_story.txt','r',encoding='cp1252') as f:
#     print(f.encoding)
#     data = f.read()
#     print(data)


with open('love_story.txt','r',encoding='cp1252') as f:
    data = f.read(100)
    while len(data) > 0:
        print(data)
        data = f.read(100)                


# ======================================================== READ CSV FILE ============================================================
from csv import reader

with open('file.csv','r') as f:
    csv_reader = reader(f)
    # it is iterator
    next(csv_reader)
    for row in csv_reader:
        print(row)
    # print(csv_reader)

# 														Read csv with Dict reader
from csv import DictReader
# order dict
with open('file.csv','r') as f:
    csv_reader = DictReader(f,delimiter='|')
    for row in csv_reader:
        print(row['email'])



# Read csv with Dict reader
from csv import DictReader
# order dict
with open('file.csv','r') as f:
    csv_reader = DictReader(f,delimiter='|')
    for row in csv_reader:
        print(row['email'])

# 																	write to csv file
# writer, DictWriter
from csv import writer
with open('file5.csv','w', newline='') as f:
    csv_writer = writer(f)
    # methods - writerow, writerows
    # csv_writer.writerow(['name','country'])
    # csv_writer.writerow(['djeq cpp','china'])
    # csv_writer.writerow(['Block_cipher','india'])
    # csv_writer.writerow(['pter','america'])


    csv_writer.writerows([['name','country'],['djeq cpp','china'],['Block_cipher','india'],['pter','america']])



# write to csv file
# writer, DictWriter
# from csv import writer
# with open('file5.csv','w', newline='') as f:
    # csv_writer = writer(f)
    # methods - writerow, writerows
    # csv_writer.writerow(['name','country'])
    # csv_writer.writerow(['djeq cpp','china'])
    # csv_writer.writerow(['Block_cipher','india'])
    # csv_writer.writerow(['pter','america'])


    # csv_writer.writerows([['name','country'],['djeq cpp','china'],['Block_cipher','india'],['pter','america']])


# ============================================= write to csv file with DictWriter ===================================================
from csv import DictWriter
with open('file3.csv', 'w',newline='') as f:
    csv_writer = DictWriter(f,fieldnames=['first_name','last_name','age'])  
    csv_writer.writeheader()
    # two method writerow ,writerows
    
    # csv_writer.writerow({
    #     'first_name':'Gaurav',
    #     'last_name':'kumar',
    #     'age' : 13
    # })

    # csv_writer.writerow({
    #     'first_name':'Block',
    #     'last_name':'Cipher',
    #     'age' : 13
    # })    
    # csv_writer.writerow({
    #     'first_name':'Stream',
    #     'last_name':'Cipher',
    #     'age' : 21
    # })    
    
# writerows method
csv_writer.writerows = ([
    {'first_name':'Gaurav','last_name':'kumar','age':13},
    {'fist_name':'Ankit','last_name':'kumar','age':8},
])

 


# ============================================================ Read and Wirte in csv file ============================================
from csv import DictReader,DictWriter
with open('file.csv','r') as rf:
    with open('file3.csv','w' ,newline='') as wf:
        csv_reader = DictReader(rf)
        csv_writer = DictWriter(wf,fieldnames=['name','country','age'])
        csv_writer.writeheader()
        for row in csv_reader:
            fname, lcountry, age = row['name'],row['country'],row['age']
            csv_writer.writerow({
                'name':fname.upper(),
                'country':lcountry.upper(),
                'age':age.upper()
            })