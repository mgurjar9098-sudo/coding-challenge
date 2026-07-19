import random

# random_number=random.random()
# print(random_number)

# random_number=random.randint(1,10)
# print(random_number)

# random_number=random.randrange(1,100)
# print(random_number)

# random_number=random.uniform(1,10)
# print(random_number)

# random_number=random.randint(1,2)
# if random_number==1:
#     print("head")
# else:
#     print('tail')


# list=["mango",'banana','apple']
# list[0]='papaya'
# list.insert(0,"grapes")
# list.append(90)
# print(list)


# random number choice friends name 

# # 1 option
# import random
# friends=['Alice',"bob","charlie","david","Emanuel"]

# random_name=random.choice(friends)
# print(random_name)

# #2 option
# random_number=random.randint(0,4)
# print(friends[random_number])


# IndexError

# fruits=['mango','banana','grapes']
# num=[11,22,33,44]
# l=[fruits,num]

# print(l[1][1])
# user=2
# print(fruits[user-1])



# rock peper scrissor

# import random

# number=int(input("what do you choose? Type for Rock 0 for Pepar 1 or 2 for Scissor "))
# print(number)
# guess=None
# if number==0:
#     guess='rock'
# elif number==1:
#     guess='paper'
# elif number==2:
#     guess='scissor'
# else:
#     print("invalid choice")
 


# list=["rock",'paper','scissor']
# computer_choice=random.choice(list)
# if guess == computer_choice:
#      print('match draw') 
# elif guess=='rock' and computer_choice=='scissor':
#     print('you win')

# elif guess=='scissor' and computer_choice=='paper':
#     print('you win')

# elif guess=='paper' and computer_choice=='rock':
#     print('you win')

# elif computer_choice=='rock' and guess=='scissor':
#     print('computer win')

# elif computer_choice=='scissor' and guess=='paper':
#     print('computer win')

# elif computer_choice=='paper' and guess=='rock':
#     print('computer win')






# prime number

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')