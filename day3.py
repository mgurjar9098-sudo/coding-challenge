# print("Welcome to the rollecoaster")
# height=int(input("what is your height in cm? "))

# if height>=120:
#     print("You can ride the rollercoaster")
# else:
#     print("Sorry you have to grow teller before you can ride. ")


# modulo operator 
# num=int(input("enter the number "))

# if num%2==0:
#     print("even")
# else:
#     print("odd")


# nested if statement 


# print("Welcome to the rollecoaster")
# height=int(input("what is your height in cm? "))

# if height>=120:
#     print("You can ride the rollercoaster")
#     age=int(input("enter the age"))
#     if age<=12:
#         print("please pay $5. ")
#     elif(age<=18):
#         print("plaese pay $7. ")
#     else:
#         print("please pay $12. ")
# else:
#     print("Sorry you have to grow teller before you can ride. ")



# if /elif/else
 

# print("Welcome to the rollecoaster")
# height=int(input("what is your height in cm? "))
# bill=0

# if height>=120:
#     print("You can ride the rollercoaster")
#     age=int(input("enter the age"))
#     if age<=12:
#         bill=5
#         print("child to pay $5")
#     elif age<=18:
#         bill=7
#         print("adult to pay $7")
#     else:
#         bill=12
#         print("you pay on $12")
#     photo=input("you want to take photo pay extra if yes to enter y otherwise no")

#     if photo=='y':
#         bill+=3
#     print(f"your total bill is ${bill}")
# else:
#     print("Sorry you have to grow teller before you can ride. ")



# Python pizza challenge

# print("Welcome to Python Pizza Deliveries !")
# size=input("what size pizaa do you want ? S, M or L : ")
# pepperoni=input("Do you want pepperoni on your pizza Y or N : ")
# extra_cheese=input("Do you want to extra cheese Y or N: ")
# bill=0


# if size=='S':
#     bill=15
#     # if pepperoni=='Y':
#         # bill+=2
    
# elif size=='M':
#     bill=20

#     # if pepperoni=='Y':
#     #     bill+=3

# elif size=='L':
#     bill=25 
#     # if pepperoni=='Y':
#     #     bill+=3

# else:
#     print("you typed the wrong inputs")


# if pepperoni=='Y':
#     if size=='S':
#         bill+=2
#     else:
#         bill+=3



# if extra_cheese=='Y':
#     bill+=1

# print(f"Your Final bill is ${bill}.")



# using logical operator

# print("Welcome to the rollecoaster")
# height=int(input("what is your height in cm? "))
# bill=0

# if height>=120:
#     print("You can ride the rollercoaster")
#     age=int(input("enter the age"))
#     if age<=12:
#         bill=5
#         print("child to pay $5")
#     elif age<=18:
#         bill=7
#         print("adult to pay $7")
    
#     if age>=45 and age <=55:
#         print("you can free ride")
#     else:
#         bill=12
#         print("you pay on $12")
#     photo=input("you want to take photo pay extra if yes to enter y otherwise no")

#     if photo=='y':
#         bill+=3
#     print(f"your total bill is ${bill}")
# else:
#     print("Sorry you have to grow teller before you can ride. ")


num1=int(input("enter the num1: "))
num2=int(input("enter the num2: "))
num3=int(input("enter the num3: "))

if num1>=num2 and num1>=num3:
    print("num1 is greater")

elif num2>=num1 and num2>=num3:
    print("num2 is greater")

else:
    print("num3 is greater")
