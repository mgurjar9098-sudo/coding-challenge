# Type Conversion= you can convert data into into different data types usign special function eg. float(),int()

# VALUE="123"
# print(type(VALUE))
# num=float(VALUE)
# print(type(num))
# print(num)



# print(type("hello"))
# print(type(123))
# print(type(33.00))
# print(type(True))

# This is a primitive data type 

# String
# Float
# INTGER
# boolean


# task-1

# print("Number of letters in your name: " + str(len(input("enter the name"))))

# Mathemtical calculations 

# print(11+12)
# print(3-3)
# print(3*3)
# print(3/3)
# print(4//3)
# print(3**3)


# PEMDAS LR
# ()
# **
# * or /
# + or -

# value=(3*3+3/3-3)
# print(value)

# value=(3*(3+3)/3-3)
# print(value)



# Number Manipulation And F String in Python

# val=int(3.1333)
# print(val)


# val=12.6444
# print(round(val))
# print(round(val,2))

# f string 
 

#  day-2
# project -2

print('welcome to the tip calculator!')
bill=float(input('what was the total bill? $'))
tip=int(input("How much tip would you like to give? 10,12,or 15: "))
people=int(input("How many people to split the bill? "))

tip_as_persent=tip/100
total_tip_amount=bill*tip_as_persent
total_bill=bill+total_tip_amount
bill_per_person=total_bill/people

print(f"Each person should pay: ${round(bill_per_person,2)}")
 
