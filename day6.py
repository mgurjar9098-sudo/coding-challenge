# lambda function

# add_value= lambda a,b:a+b
# print(add_value(11,44))

# # same 

# def add_value(a,b):
#     return a+b


# print(add_value(11,44))



# *args

# def value_args(*args):
#     return args


# print(value_args(11,22,33,44,55,66))


# def value(**kwargs):
#     for key,value in kwargs.items():
#         print(key,value)


# value(name="ram",age=22)


# def both(*args, **kwargs):
#     for i in args:
#         print(i,end=" ")
#     for key ,value in kwargs.items():
#         print(key,value)


# both(32,44,name='ram',age=33)


# local variable and global variable 

# x=10

# def add():
#     global x
#     x=20
#     print(x)


# add()
# print(x)


# recursion fuction


# def factorial(num):
#     if num==1 or num==0:
#         return 1
#     else:
#         return num * factorial(num-1)

# print(factorial(5))


# without map function

def myfun(v):
    return len(v)


# test=["apple",'banana','mango']
# lst=[]

# for i in test:
#     lst.append(myfun(i))

# print(lst)
# test=["apple",'banana','mango']
# x=map(myfun,test)
# print(list(x))



# filter 

# def great(a):
#     if a>20:
#         return a
# l=[22,33,44,5,11,22,33]
# y=filter(great,l)
# print(list(y))


# def checkeven(num):
#     if num%2==0:
#         return num
        

# list1=[33,44,55,66,77,88]

# x=filter(checkeven,list1)
# print(list(x))

# from functools import reduce

# list1=[1,2,3,4,5,6,7,8]

# def value(a,b):
#     return a+b

# x=reduce(value,list1)
# print(x)



# positonal argument

# positional arguments mean same order of arguments and same order or perameter

# same order of arguments and perameter

# def add(a,b):
#     return a+b

# print(add(10,20))

# 3️⃣ Keyword Arguments (Order Does NOT Matter)
# def info(name,age):

#     print(f"name is {name} and age is {age}")

# keyword arguments
# info(age=33,name="mohan")



# 4️⃣ Mixing Positional + Keyword Arguments

# def value(name,age=16):
#     print(f"name is {name} and age is {age}")


# value('mohan',45)


# def value(a,b=2):
#     return a**b

# print(value(2))
# print(value(3,3))



# def add(item,lst=None):
#     if lst==None:
#         lst=[]
#     lst.append(item)
#     return lst


# print(add(11))



# def info(name,*,age,city):
#     print(f"name is {name} age is {age} and city is {city}")


# info(name='rahul',age=16,city='mds')



# lambda function deep dive


# x=lambda a:a*a

# print(x(20))

# x=lambda a,b:a if a>b else b
# print(x(330,44))

# num=lambda num:print("even") if num%2==0 else print("odd")
# num(12)
# num(13)

# value=lambda x:(x+2,x**2,x*2)[-1]
# print(value(3))


# built in function with lambda

# num=[1,2,3,4]
# value=list(map(lambda x: x*x,num))
# print(value)

# num=[2,3,4,6,7,8,9]

# value=list(filter(lambda x:x%2==0,num))
# print(value)


# from functools import reduce
# num=[1,2,3,4,5]
# value= reduce(lambda a,b:a+b,num)
# print(value)


# students = [("Raj", 21), ("Amit", 20), ("Neha", 22)]
# value=sorted(students,key=lambda x:x[0])
# print(value)


# lambda with default value

# value=lambda x,y=20:x+y

# print(value(20))
# print(value(10,40))


# nested lambda

# make_power=lambda n:(lambda x:x**n)

# square=make_power(2)
# cube=make_power(3)

# print(square(4))
# print(cube(3))


# iterator 

# name="mohan"
# nm=iter(name)

# print(nm.__next__())
# print(nm.__next__())
# print(nm.__next__())
# print(nm.__next__())
# print(nm.__next__())

# dict={
#     'name':'ram',
#     'city':'mds',
#     'age':16
# }


# value=iter(dict.items())
# print(value.__next__())

# list=[11,22,33,44]

# v=iter(list)
# print(v.__next__())
# print(v.__next__())

# list=[11,22,33,44]
# v=iter(list)
# while True:
#     try:
#          print(v.__next__())
#     except StopIteration:
#         print('iterator is end')
#         break



# custom iter

# class odd_number:
#     def __iter__(self):
#         self.n=1
#         return self
    
#     def __next__(self):
#         x=self.n
#         self.n+=2
#         return x


# num=odd_number()
# value=iter(num)
# print(value.__next__())
# print(value.__next__())
# print(value.__next__())
# print(value.__next__())
# print(value.__next__())




# generator

# def test():
#     yield 1
#     yield 2
#     yield 3

# t=test()
# print(next(t))
# print(next(t))
# print(next(t))
    


# def test(max):
#     cnt=1
#     while cnt<=max:
#         yield cnt
#         cnt+=1

# t=test(10)
# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t))


# def fib(num):
#     a=0
#     b=1
#     i=1
#     while(i<=num):
#         c=a+b
#         yield c
#         a=b
#         b=c
#         i=i+1


# num=fib(10)
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))




def even_number():
   i=0
   while True:
    i=i+2
    yield i
        
        
    

obj=even_number()
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))


# print(even_number(10))















