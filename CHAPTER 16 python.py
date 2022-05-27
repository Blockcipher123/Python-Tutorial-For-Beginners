# **********************************************************************************************************************************************************
# **********************************************************************************************************************************************************
# *******************************************************************CH - 16***********************************************************************************
# **********************************************************************************************************************************************************
# **********************************************************************************************************************************************************
# **********************************************************************************************************************************************************


# =================================================== OBJECT ORIENTED PROGRAMMING ====================================================

# COMMON TOPIC IN ALMOST ALL POPULAR PROGRAMMING LANGUAGE(PYTHON, C++,JAVA)
# WITH COMMON IDEA BUT WITH DEFFERENT SYNTEX

# OPP IS JUST A STYLE/WAY TO WRITE A CODE

# VERY HELPFULL IN CREATING REAL WORLD PROGRAM

# WE WILL SEE OTHER ADVENTAGES WHEN WE WILL START LEARNING OPP

# class , object(instance), mehtod

# list object
# list object
# method

l = [1,2,3,4]
l2 = [5,6,7,8,9]
l3 = ['Gaurav kumar']
l.pop(2)

# 														opp creat your first class
# OBJECTIVE 
# WHAT IS CLASS 
# HOW TO CREAT AN CLASS 
# WHAT IS INIT METHOD, is also know as constuctor 
# WHAT ARE ATTRIBUTES, INSTANCE VERIABLES


class Person:
    def __init__(self, first_name,last_name,age):
        # instance variable
        print('init method called')
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


# Here is object
p1 = Person('Gaurav','kumar',13)
p2 = Person('mohit','kumar',19)

print(p1.first_name)
print(p2.first_name)


# 														exercise of ch 16
# creat a laptop class with Attribute like brang name, model_name, price
# creat two object/instance of your laptop class

class Laptop:
    def __init__(self, name , model_name,price):
        print('laptop details')
        self.name = name
        self.model_name = model_name
        self.price = price
        self.laptop_name = name + ' ' + model_name 

l1 = Laptop('ASUS','au114tx', 20000)       
l2 = Laptop('LEVONO','', 3000)

# print(l1.name)
# print(l1.model_name)
# print(l1.price)

# print(l2.name)
# print(l2.model_name)
# print(l2.price)

print(l1.laptop_name)


# opp - instance method
class Person:
    def __init__(self, first_name, last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f'{self.first_name} {self.last_name} {self.age}'
    def is_above_18(self):
        return self.age>18


p1 = Person('Gaurav','kumar',13)
p2 = Person('mohit','kumar',30)
# print(p1.full_name())
print(Person.full_name(p2))
print(Person.is_above_18(p2))

# exercise2 ch 16
# def a function which can find percentage 


class Laptop:
    def __init__(self, name , model_name,price):
        # print('laptop details')
        self.name = name
        self.model_name = model_name
        self.price = price
        self.laptop_name = name + ' ' + model_name 

    def percentage_off(self,number):
        # self.price
        off_price = (number/100)*self.price
        return self.price - off_price



l1 = Laptop('ASUS','au114tx', 62000)      
l2 = Laptop('Apple','macbook pro', 320000)  
# l2 = Laptop('LEVONO','', 300
print(l1.percentage_off(20))
print(l2.percentage_off(20))


# exercise2 ch 16
# def a function which can find percentage 

class Laptop:
    descount_percent = 100
    def __init__(self, name , model_name,price):
        # print('laptop details')
        self.name = name
        self.model_name = model_name
        self.price = price
        self.laptop_name = name + ' ' + model_name 

    def percentage_off(self):
        # self.price
        off_price = (Laptop.descount_percent/100)*self.price
        return self.price - off_price



l1 = Laptop('ASUS','au114tx', 62000)      
l2 = Laptop('Apple','macbook pro', 320000)  

# l2 = Laptop('LEVONO','', 300
print(l1.percentage_off())
print(l2.percentage_off())

# opp class veriable 
# circle veriable
# circle 
# area

class Circle:
    pi = 3.14
    # area = 3.14*self.redius **2

    def __init__(self,redius):
        self.redius = redius
        # self.area = area
        # self.pi = pi

    def calc_circumference(self):
        return 2*Circle.pi*self.redius

c2 = Circle(4)
c = Circle(45)
c1 = Circle(456)

print(c2.calc_circumference())
print(c.calc_circumference())
print(c1.calc_circumference())



# opp class veriable part 2
class Laptop:
    descount_percent = 5
    def __init__(self, name , model_name,price):
        # print('laptop details')
        self.name = name
        self.model_name = model_name
        self.price = price
        self.laptop_name = name + ' ' + model_name 

    def percentage_off(self):
        # self.price
        off_price = (self.descount_percent/100)*self.price
        return self.price - off_price

# this is for we can change the dicount 0
# Laptop.descount_percent = 5

l1 = Laptop('ASUS','au114tx', 62000)      
l2 = Laptop('Apple','macbook pro', 320000) 
l2.descount_percent = 50

# l2 = Laptop('LEVONO','', 300
print(l1.percentage_off())
print(l2.percentage_off()) 
# print(l1.__dict__)
print(l2.__dict__)


# 															exercise 3 ch 16
class Person:
    Person_count = 0

    def __init__(self, first_name, last_name, age):
        Person.Person_count += 1
        self.first_name = first_name 
        self.last_name = last_name
        self.age = age 

    # def Person_count(self):
    #     count_object = (self count_object.count)self.age


p1 = Person(
    'remesh','kumar',24
)
p2 = Person(
    'Mohan','kumar',19
)

print(Person.Person_count)


# 																opp - class method
# difference between class method and instance method
class Person:
    count_instance = 0
    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name 
        self.last_name = last_name
        self.age = age

    @classmethod
    def count_instances(cls):
        return f'You have created {cls.count_instance} instences of {cls.__name__} class'   

    def full_name(self):
        return f'{self.first_name} {self.last_name}'      

    def is_above_18(self):
        return self.age>18

p1 = Person('Gaurav','kumar', 13)
p2 = Person('amit', 'kumar', 20)
print(Person.count_instances())     


# opp - class  method as constuctor

class Person:
    count_instance = 0
    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name 
        self.last_name = last_name
        self.age = age


    @classmethod
    def from_string(cls,string):
        first,last,age = string.split(',')
        return cls(first,last,age)

    @classmethod
    def count_instances(cls):
        return f'You have created {cls.count_instance} instences of {cls.__name__} class'   

    def full_name(self):
        return f'{self.first_name} {self.last_name}'      

    def is_above_18(self):
        return self.age>18

p1 = Person('Gaurav','kumar', 13)
p2 = Person('amit', 'kumar', 20)
p3 = Person.from_string('Block, Cipher,13')
print(p3.full_name())
print(Person.count_instances()) 


# opp static mehtod


class Person:
    count_instance = 0
    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name 
        self.last_name = last_name
        self.age = age


    @classmethod
    def from_string(cls,string):
        first,last,age = string.split(',')
        return cls(first,last,age)

    @classmethod
    def count_instances(cls):
        return f'You have created {cls.count_instance} instences of {cls.__name__} class'   

    @staticmethod
    def hello():
        print('hello, static method called')    

    def full_name(self):
        return f'{self.first_name} {self.last_name}'      

    def is_above_18(self):
        return self.age>18

# p1 = Person('Gaurav','kumar', 13)
# p2 = Person('amit', 'kumar', 20)
p3 = Person.from_string('Block, Cipher,13')
Person.hello()
# print(Person.count_instances()) 


# 														encapsulation, Abstraction,naming convntions , Name mangling
# In this video we will talk about 
# encapsulation 
# Abstraction
# some special naming convention 
# Name mangling, __name (not a covenction)

class Phone:
    def __init__(self, brand,model_name ,price):
        self.brand = brand
        self.model_name = model_name
        self.__price = price

    
    def make_a_call(self,Phone_number):
        print (f'calling {Phone_number} ...')

    def full_name(self):
        return f'{self.brand}{self.model_name}'

    def send_massage(self):
        pass # twilio

# _name # convetion of private name
# __name__ # dunder/magic method
phone1 = Phone('nokia','1100',1000)
# print(phone1.__price)
print(phone1._Phone__price)
phone1._Phone__price = -1000
print(phone1._Phone__price)
# print(phone1.__dict__)   
# phone1._price = -10000
# print(phone1._price)


# l = [2,3,1,4]
# l.sort() # we can use this in python tim sort
# print(l)        
   # 															property , setter decoraters
# will discuss three problem in existing
# them we will solve them using getter , setter decoraters
class Phone:
    def __init__(self, brand,model_name ,price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)
        # if price > 0 :
        #     self._price = price
        # else:
        #     self._price = 0          
        # self.complete_specification = f'{self.brand} {self.model_name} and price is {self._price}'
    @property
    def complete_specification(self):
        return f'{self.brand} {self.model_name} and price is {self._price}'

    # getter(), setter 
    @property
    def price(self):
        return self._price    

    @price.setter
    def price(self,new_price):
        self._price = max(new_price,0) 

    def make_a_call(self,Phone_number):
        print (f'calling {Phone_number} ...')

    def full_name(self):
        return f'{self.brand}{self.model_name}'

phone1 = Phone('nokia', '1100', 1000)
phone1.price = -500
print(phone1.price)
print(phone1.complete_specification)



# 																	inheritance intro
class Phone:
    def __init__(self, brand,model_name ,price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)


    def full_name(self):
        return f'{self.brand}{self.model_name}'        

    def make_a_call(self,Phone_number):
        print (f'calling {Phone_number} ...')



class Smartphone(Phone): # derived / child class
    def __init__(self, brand,model_name ,price,ram, internal_memory, rear_camera): 
        # two type we can do that
        # Phone.__init__(self, brand,model_name ,price) # uncommon way
        super().__init__(brand,model_name ,price)
        self.ram = ram  
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera


    

phone = Phone('ASUS', ' zeon phone max pro m1', 15000)
smartphone = Smartphone('Apple', ' i phone 12 pro', 150000, '8 GB','128 GB', '12 MP')
print(phone.full_name())
print(smartphone.full_name() + f' and price is {smartphone._price}')




# 									more about 	inheritance, multileve inheritance, MRO, method overriding, etc.
# can we derive more than one class form base class?
# multilevel inheritance
# method resolutin order
# method overriding
# isinstance(), issubclass()
# inheritance intro



class Phone:
    def __init__(self, brand,model_name ,price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)


    def full_name(self):
        return f'{self.brand}{self.model_name}'        

    def make_a_call(self,Phone_number):
        print (f'calling {Phone_number} ...')



class Smartphone(Phone): # derived / child class
    def __init__(self, brand,model_name ,price,ram, internal_memory, rear_camera): 
        # two type we can do that
        # Phone.__init__(self, brand,model_name ,price) # uncommon way
        super().__init__(brand,model_name ,price)
        self.ram = ram  
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

    def full_name(self):
        return f'{self.brand} {self.model_name} price is {self._price} ram is {self.ram} rear_camera {self.rear_camera}'



class FlagshipPhone(Smartphone):
	def __init__(self, brand,model_name ,price,ram, internal_memory, rear_camera, front_camera, processer): 

		super().__init__(brand,model_name ,price,ram, internal_memory, rear_camera)
		self.front_camera = front_camera
		self.processer = processer  



    # def full_name(of):
    #     return f'{self.brand} {self.model_name} price is {self._price} ram is {self.ram} rear_camera is {self.rear_camera} front_camera {self.front_camera} and processer is = {self.processer}' 
    
   


    

# phone = Phone('ASUS', ' zeon phone max pro m1', 15000)
smartphone = Smartphone('Apple', ' i phone 12 pro', 150000, '8 GB','128 GB', '12 MP')
flagshipPhone = FlagshipPhone('opePlus', ' 5pro', 150000, '8 GB','128 GB', '64 MP' ,'20 MP', 'G85')
# print(phone.full_name())
# print(smartphone.full_name() + f' and price is {smartphone._price}')
# print(flagshipPhone.full_name() + f' and processer is {flagshipPhone.processer}')
# print(flagshipPhone.full_name())
# print(help(FlagshipPhone))
print(isinstance(smartphone, FlagshipPhone))
# issubclass
print(issubclass(Smartphone, Phone))



# multiple inheritance


class A:
    def class_a_method(self):
        return "I/m'just a class A method "

    def hello(self):
        return 'hello from class A'    

class B:
    def class_b_method(self):
        return "I/m'just a class B method "

    def hello(self):
        return 'hello from class B'            



class C(B,A):
    pass

instance_c = C()
# print(instance_c.class_a_method())
# print(instance_c.class_b_method())
# print(instance_c.hello())
print(instance_c.hello())
print(instance_c.hello())
print(help(C))
print(C.mro())
print(C.__mro__)


# 													magic / dunder methods, 
# operator overloadingm,
#  polymorphism, method overriding


class Phone:
    def __init__(self, brand,model_name ,price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)


    def full_name(self):
        return f'{self.brand}{self.model_name}'   

    # we can use two dunder method for these
    # str , repr
    
    def __repr__(self):
        return f"{self.brand} {self.model_name} and price is {self._price}"
    def __str__(self):
        return f"Phone (\'{self.brand}\', \'{self.model_name}\', \'{self._price}\')"

    def __len__(self):
        return len(self.full_name())

    def __mul__(self, other):
        return self._price * other._price

class SmartPhone(Phone):
    def __init__(self, brand, model_name, price, camera):
        super().__init__(brand,model_name ,price)
        self.camera = camera

    def full_name(self):
        return f'{self.brand} {self.model_name} and price is {self._price}'    

    def __len__(self):
        return self._price





# l = [1,2,3]
# print(l)        


my_phone = Phone('nokia', '1100', 1000)
my_phone2 = Phone('nokia', '1700', 2000)
my_smartphone = SmartPhone('realme', ' c15', 12000 ,'12 MP')
print(my_smartphone.full_name())
print(my_phone.full_name())
print(len(my_smartphone))
print(len(my_phone))




# print(my_phone * my_phone2)
# print(len(my_phone))
# print(str(my_phone))
# print(repr(my_phone))