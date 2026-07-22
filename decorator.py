
# simple decorator

# def decorator(fun):
#     def wrapper():
#         print("this is start the code")
#         fun()
#         print("this is end the code")
    
#     return wrapper

# @decorator
# def greet():
#     print("hello world !")

# greet()


# decorator with arguments


# def decorator(fun):
#     def wrapper(a,b):
#         print("welcome the program")
#         fun(a,b)
#         print('end program! coming back again')
#         return a+b
#     return wrapper


# @decorator
# def add(a,b):
#     print(f"addition is two number {a+b}")


# add(11,22)



# decorator with arguments

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Before")
#         func(*args, **kwargs)
#         print("After")
#     return wrapper

# @decorator
# def add(a, b):
#     print(a + b)

# add(10, 20)

# muliple decorator

# def star(func):
#     def wrapper():
#         print("*****")
#         func()
#         print("*****")
#     return wrapper

# def hash_symbol(func):
#     def wrapper():
#         print("#####")
#         func()
#         print("#####")
#     return wrapper

# @star
# @hash_symbol
# def hello():
#     print("hello")

# hello()



# method decorator 
# def method_decorator(fun):
#     def wrapper(self,*args, **kwargs):
#         print("start the method decorator")
#         res=fun(self ,*args, **kwargs)
#         print("end the method decorator")
#         return res
#     return wrapper

# class myclass:
#     @method_decorator
#     def say_hello(self):
#         print('hello method decorator')


# obj=myclass()
# obj.say_hello()



# class decorator

# def fun(cls):
#     cls.class_name = cls.__name__
#     return cls

# @fun
# class Person:
#     pass

# print(Person.class_name) 


# @staticmethod
# Class ke andar aisa method jo object (self) ya class (cls) ki zarurat nahi rakhta.

# class Demo:

#     @staticmethod
#     def hello():
#         print("Hello")

# Demo.hello()

# @classmethod
# Ye class ko (cls) first argument ke roop me receive karta hai.

# class Student:

#     school = "ABC School"
#     @classmethod
#     def show(cls):
#         print(cls.school)

# Student.show()


# class method decorator

# class student:
#     school_name='goverment high school'

#     @classmethod
#     def show(cls,new_name):
#         cls.school_name=new_name
#         return cls.school_name

# print(student.show("new government high school"))


#  @property
# Method ko property ki tarah access karne ke liye use hota hai.

# class Student:
#     def __init__(self, marks):
#         self._marks = marks

#     @property
#     def marks(self):
#         return self._marks

# s = Student(95)
# print(s.marks)


# class student:
#     def __init__(self,first,last):
#         self.first=first
#         self.last=last

#     @property
#     def email(self):
#         return f"{self.first}@{self.last}example.com"
    

    
# obj=student('rahul','sharma')

# print(obj.email)


# using gatter setter and deleter
class student:
    def __init__(self,marks):
        self._marks=marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self,value):
        if value< 0 or value > 100:
            print("invalid marks")
        else:
            self._marks=value

    @marks.deleter
    def marks(self):
        del self._marks
        

s=student(80)
s.marks=120

# del s.marks

print(s.marks)