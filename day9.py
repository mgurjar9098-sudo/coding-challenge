#Write a Python program to check if a number is positive, negative or zero. 

# num=int(input("enter the number"))

# if num>0:
#     print('positive')
# elif num<0:
#     print('negetive')
# else:
#     print('zero')


#  Write a Python program to get the Factorial number of given number. 

# num=int(input("enter the number"))

# fact=1
# for i in range(1,num+1):
#     fact=fact*i

# print("Factorial is ",fact)



# Write a Python program to get the Fibonacci series of given range.  

# num=int(input("enter the number"))
# a=-1
# b=1
# i=1
# while(i<=num):
#     c=a+b
#     print(c,end=" ")
#     a=b
#     b=c

#     i=i+1


# Write python program that swap two number with temp variable and 
# without temp variable. 


# with temp varible 
# num1=int(input("enter the first number "))
# num2=int(input("enter the second number "))

# print(f"num1 is ",num1)
# print(f"num1 is ",num2)

# temp=num1
# num1=num2
# num2=temp

# # print('with temp varible')
# # print(f"num1 is ",num1)
# # print(f"num1 is ",num2)

# num1,num2=num2,num1
# print('without temp varible')
# print(f"num1 is ",num1)
# print(f"num1 is ",num2)


# num=int(input('enter the number'))

# if num%2==0:
#     print('number is even number')

# else:
#     print("number is odd number")


# Write a Python program to test whether a passed letter is a vowel or 
# not. 

# char=input("enter the char")

# if char=='i' or char=='a' or char=='e' or char=='o' or char=='u' or char=='I' or char=='A' or char=='E' or char=='O' or char=='U' :
#     print('vowel')
# else:
#     print('not vowel')

#  Write a Python program to sum of three given integers. However, if 
# two values are equal sum will be zero.  

# num1=int(input("enter the first number "))
# num2=int(input("enter the second number "))
# num3=int(input("enter the third number "))

# if num1==num2 or num1==num3  or num2==num3:
#     print('0')
# else:
#     print(num1+num2+num3)



# Write a Python program that will return true if the two given integer 
# values are equal or their sum or difference is 5. 


num1=int(input('enter the first number'))
num2=int(input('enter the second number'))

if num1==num2 or num1+num2==5 or num1-num2==5:
    print(True)

else:
    print(False)













