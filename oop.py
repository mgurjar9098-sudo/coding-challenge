# class student:

#     def __init__(self,name,last):
#         self.name=name
#         self.last=last



# s=student("ram",'gurjar')
# print(s.name)
# print(s.last)


# class student:

#     def __init__(self,name,last):
#         self.name=name
#         self.last=last

#     def show(self):
#         print(f"name is {self.name} and last name is {self.last}")



# s=student("ram",'gurjar')
# s.show()



# class voter:

#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def show(self):
#         print(f"your name is {self.name} and age is {self.age}")

#     def is_above(self):
#         if self.age>=18:
#             return True
#         else:
#             return False

# v=voter("ram",18)
# print(v.is_above())
# v.show()


# class varible
# class Circle:
#     pi=3.14
#     def __init__(self,redius):
#         self.redius=redius

#     def cir_refrece(self):
#         return 2*self.pi*self.redius

# c=Circle(3)
# print(c.cir_refrece())



# return data in dictinary formate

# class person:

#     def __init__(self,name,age,city):
#         self.name=name
#         self.age=age
#         self.city=city


# p=person("mohan",18,'mds')
# print(p.__dict__)


# class student:
#     name='government'

#     @classmethod
#     def show_name(cls):
#         print("this is class method")
#         print(cls.name)

# student.show_name()



# class student:
#     count=0
#     def __init__(self,name):
#         student.count+=1
#         self.name=name

#     @classmethod
#     def count_obj(cls):
#         return cls.count

# s=student('ram')
# s2=student('mohan')
# s3=student('richa')
# print(student.count_obj())


# Class method as constctor

# class student:

#     def __init__(self,name,age,roll):
#         self.name=name
#         self.age=age
#         self.roll=roll

#     def detail(self):
#         print(f"name is {self.name} and age is {self.age} and {self.roll}")

#     @classmethod
#     def from_string(cls,string):
#         name,age,roll=string.split()
#         return cls(name,age,roll)
# s=student('ram',32,101)
# s1=student.from_string('mohan 34 102')
# s.detail()
# s1.detail()



# static method
# class Person:

#     @staticmethod
#     def show():
#         print("this is static method")

# # obj=Person()
# # obj.show()

# Person.show()



# getter and setter method in oops
# class person:

#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age

#     def get_name(self):
#         return self.__name

#     def set_name(self,name):
#         if isinstance(name,str) and len(name)>0:
#             self.__name=name
#         else:
#             print("invalid name please enter valid name")

#     def get_age(self):
#         return self.__age

#     def set_age(self,age):

#         if isinstance(age,int) and age>0:
#             self.__age=age
#         else:
#             print("invalid age")

# p=person("ram",18)
# print(p.get_name())
# print(p.get_age())

# p.set_age(22)
# print(p.get_age())

# p.set_name('mohan')
# print(p.get_name())


# single level inheritence



# class phone:

#     def __init__(self,brand_name,model,price):
#         self.brand_name=brand_name
#         self.model=model
#         self.price=price

#     def detail(self):
#         print(f"mobile name is {self.brand_name} and brand {self.brand_name} and price {self.price}")

# class smartPhone(phone):
#     def __init__(self,brand_name,model,price,cam):
#         super().__init__(brand_name,model,price)
#         self.cam=cam

#     def detail(self):
#         print(f"mobile name is {self.brand_name} and brand {self.model} and price {self.price} and cam is {self.cam}")


# s=smartPhone('vivo','y14',12000,'15px')
# s.detail()



# second method

# class phone:

#     def __init__(self,brand_name,model,price):
#         self.brand_name=brand_name
#         self.model=model
#         self.price=price

#     def detail(self):
#         print(f"mobile name is {self.brand_name} and brand {self.brand_name} and price {self.price}")

# class smartPhone(phone):
#     def __init__(self,brand_name,model,price,cam):
#         phone.__init__(self,brand_name,model,price)
#         self.cam=cam

#     def detail(self):
#         print(f"mobile name is {self.brand_name} and brand {self.model} and price {self.price} and cam is {self.cam}")


# s=smartPhone('oppo','z5',15000,'50px')
# s.detail()



# multilevel inheritence:

# class GrandFather:
#     def  display_grand(self):
#         print("This is grand father class")


# class Father(GrandFather):

#     def display_father(self):
#         print("this is father class")


# class Son(Father):

#     def display_son(self):
#         print("this is son class")

    
# c=Son()
# c.display_son()
# c.display_father()
# c.display_grand()



# multiple inheritence 

# class Father:

#     def father(self,fname):
#         self.fname=fname
      

# class Mother(Father):
#         def Mother(self,mname):
#             self.mname=mname
            

# class Son(Mother):
#         def son(self,sname):
#             self.sname=sname

#         def detail(self):
#             print(f'student name is {self.sname}')
#             print(f'father name is {self.fname}')
#             print(f'mother name is {self.mname}')

# s=Son()
# s.father("ashok")
# s.Mother('radharaman bai')

# s.son('rahul')
# s.detail()


# abstarcation

# from abc import ABC,abstractclassmethod

# class Vahicle(ABC):

#     @abstractclassmethod
#     def start():
#         pass

    
#     @abstractclassmethod
#     def stop():
#         pass


# class Bike(Vahicle):

#     def start(self):
#         print('bike is start')

#     def stop(self):
#         print('bike is stop')


# class Car(Vahicle):

#     def start(self):
#         print('car is start')

#     def stop(self):
#         print('car is stop')

# b=Bike()
# b.start()
# b.stop()

# c=Car()
# c.start()
# c.stop()
    



# polymorphism

# method overiding

# class A:

#     def display(self):
#         print("a is calling")


# class B(A):

#     def display(self):
#         print("b is calling")


# obj=B()
# obj.display()



# method overloading


# using default value
# class add:

#     def add_num(self,a=0,b=0):
#         print(a+b)


# obj=add()
# obj.add_num()



# using *args

# class Add:

#     def add_num(self,*args):

#         print(sum(*args))


# obj=Add()

# obj.add_num((11,22,33))


# using  **kwargs

# class info:

#     def detail(self,**kwargs):

#         for i in kwargs:
#             print(f"{i}:{kwargs[i]}")


# obj=info()
# obj.detail(name="ram",age=22,roll=103)



# class Phone:
#     def __init__(self,brnad_name,model_name,price):
#         self.brand_name=brnad_name
#         self.model_name=model_name
#         self.price=price
#     def full_details(self):
#         return f"your Phone Details {self.brand_name} {self.model_name} {self.price}"

# class SmartPhone(Phone):
#     def __init__(self, brnad_name, model_name, price,cam):
#         super().__init__(brnad_name, model_name, price)
#         self.cam=cam
#     def full_details(self):
#         return f"your Phone Details {self.brand_name} {self.model_name} {self.price} {self.cam}"

# class Flagship(SmartPhone):
#     def __init__(self, brnad_name, model_name, price, cam,ram):
#         super().__init__(brnad_name, model_name, price, cam)
#         self.ram=ram
        
# F1=Flagship("Nokia",'3310',3000,'12mp','2gb')
# S1=SmartPhone("Nokia",'3310',3000,'12mp')


# print(isinstance(F1,Phone))
# print(isinstance(S1,Flagship))
    
# print(issubclass(Flagship,SmartPhone))
# print(issubclass(Phone,SmartPhone))


# megic method and dunder method 

# class Person:
#     def __init__(self,fname,lname,age):
#         self.fname=fname
#         self.lname=lname
#         self.age=age
#     def __str__(self):
#         return f"{self.fname} {self.lname} {self.age}"
#     def __repr__(self):
#         return f"{self.fname} {self.lname} {self.age}"

# # lst=[1,2,4]
# # print(lst)
# P1=Person("Chirag","Joshi",90)
# print(P1)



class Person:
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age
    def __add__(self,other):
        return self.age+other.age
    def __eq__(self, other):
        return self.age == other.age
    
    def __len__(self):
        return len(self.fname)
    

    def __getitem__(self, index):
        return self.fname[index]
    
    def __setitem__(self, value):
        self.fname = value

    def __str__(self):
        return f"{self.fname} {self.lname} {self.age}"


P1=Person("Chirag","Joshi",91)
P2=Person("Chirag","Joshi",90)

print(P1+P2)
print(P1==P2)
print(len(P1))
print(P1[2])
P1="test"
print(P1)








