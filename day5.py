# for loop 

# fruites=['mango','banana','grapes']

# for fruit in fruites:
#     print(fruit)
#     print(fruit + " pie")


# print(fruites)


score=[10,20,30,40,50,60,70,80,90,100]


 



# total=sum(score)
# print(total)
# sum=0

# for sc in score:
#     sum=sum+sc

# print("Score is ",sum)

# max_value=max(score)
# print(max_value)

# ckeck the max value 

# max_value=0
# for sc in score:
#     if sc>max_value:
#         max_value=sc
# print(max_value)


# check the min value

# min_value=score[0]
# for sc in score:
#     if sc<min_value:
#         min_value=sc

# print(min_value)


# range function

# syntex
# range(start,stop,step)
# start=including
# stop=excluding
# step=optional

# for i in range(5):
#     print(i)



# for i in range(1,10):
#     print(i)


# for i in range(1,10,2):
#     print(i)

# import random
# letter1=['A''B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','U','V','W','X','Y','Z']
# symbol1=['?','/',']','}','[','{',')','(']
# number1=['1','2','3','4','5','6','7','8','9','0']

# password=" "

# # letter=int(input("enter the letter you want to password"))
# # symbol=int(input("enter you want to letter"))
# # number=int(input("you want to number"))


# # for i in range(0,letter):
# #     password+=random.choice(letter1)


# # for i in range(0,symbol):
# #     password+=random.choice(symbol1)

# # for i in range(0,number):
# #     password+=random.choice(number1)

# # print(f"your password is {password}")



# hard level

import random
letter1=['A''B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','U','V','W','X','Y','Z']
symbol1=['?','/',']','}','[','{',')','(']
number1=['1','2','3','4','5','6','7','8','9','0']

password=" "

letter=int(input("enter the letter you want to password"))
symbol=int(input("enter you want to letter"))
number=int(input("you want to number"))


password_list=[]
for i in range(0,letter):
    password_list.append(random.choice(letter1))


for i in range(0,symbol):
    password_list.append(random.choice(symbol1))

for i in range(0,number):
    password_list.append(random.choice(number1))


print(password_list)
random.shuffle(password_list)
print(password_list)


password=""
for char in password_list:
    password+=char


print(f"your password is {password}")




