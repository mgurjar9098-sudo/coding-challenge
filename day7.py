# f=open('example.txt','w')
# f.write("hello world")

# f=open('1st.txt')
# print(f.tell())
# print(f.read())
# print(f.tell())
# print(f.read())
# f.seek(0)
# print(f.tell())
# print(f.read())


# f=open('1st.txt')
# print(f.read())
# print(f.readline())
# print(f.readlines())
# lines=f.readlines()
# for i in lines:
#     print(i)

# print(f.closed)
# f.close()
# print(f.closed)


# with open("1st.txt",'r')as f:
#     print(f.read())


# with open("1st.txt",'w')as f:
#     f.write("welocome to java programing")

# with open("1st.txt",'a')as f:
#     f.write("hello gaming industry")

# with open("1st.txt",'a+')as f:
#     f.seek(0)
#     print(f.read())
#     f.write("hello ai  industry")


# with open('1st.txt','r+')as f:
#     print(f.read())
#     f.write("IT is powerfull industry").


# with open('1st.txt','w+')as f:
#     f.write("IT is powerfull industry")
#     f.seek(0)
#     print(f.read())


import json
user_data={}

user_data['name']=input("enter name: ")
user_data['age']=int(input('enter age: '))
user_data['city']=input('enter city name: ')

with open('user_data.json','w')as file:
    json.dump(user_data,file,indent=4)

print("data added")












