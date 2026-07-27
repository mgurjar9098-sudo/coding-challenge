# simple 
# a=10
# b=0
# try:
#     c=a/b
#     print(c)
# except:
#     print('invalid devided')


# a=10
# b=0
# try:
#     c=a/b
#     print(c)
# except ZeroDivisionError:
#     print('0')


# a=10
# b=0
# try:
#     c=a/b
#     print(c)
# except ZeroDivisionError as obj:
#     print(obj)



# 1 Zero devision error

# hendle multiple exacption in one excaption using tuple
# a=10
# b=0
# try:
#     # c=a/b
#     c=a/n
#     print(c)
# except (ZeroDivisionError,NameError)as obj:
#     print(obj)



#2 value error

# try:
#     c=int(input('enter your number : '))
#     print(c)
# except ValueError as obj:
#     print(obj)
# print('program ended')


#3 IndexError

# name="ram"

# try:
#     print(name[3])
# except IndexError as obj:
#     print(obj)


# 4 key error

# student={
#     'name':'ram',
#     'roll':101,
#     'age':18
# }


# # print(student['course'])
# try:
#    print(student['course'])
# except KeyError as obj:
#     print(obj,'key is not define')


# file not found error

# try:
#     with open('first.txt','r')as f:
#         print(f.read())
# except FileNotFoundError as obj:
#     print(obj)

# print('program is ended')



# type error 

# a='abc'
# b=10
# try:
#     print(a+b)
# except TypeError as obj:
#     print(obj)

# print("program is ended ")



# AttributeError 

# class myclass:

#     def greet(self):
#         print("good morning all of you")

# try:
#     m=myclass()
#     m.display()
# except AttributeError as obj:
#     print(obj)

# finally:
#     print("it is funnaly block")


# Nameerror

# try:
#     a=10
#     b=0
#     c=a/b
# except NameError as obj:
#     print(obj)
# except ZeroDivisionError as ob:
#     print(ob)

# except NameError as o:
#     print(o)
# else:
#     print(c)
# finally:
#     print('end of the program')



# custom exaception
# def check_age(age):
#     if age<0 or age>100:
#         raise TypeError("invalid age")
#     else:
#         print(f"user age is {age}")

# try:
#     age=101
#     check_age(age)
# except TypeError as obj:
#     print(obj)




    




    













