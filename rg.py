# import re


# text='I love python'
# result=re.search('python',text)
# print(result)
# print(result.group())


# result=re.search('java',text)
# print(result) #it return none


# this return first value of text

# text ='python java python'
# result=re.search('python',text)
# print(result.group())


# # if return all match value

# result=re.findall('python',text)
# print(result)


# check at the begining

# text='python i love python'
# result=re.match('python',text)
# print(result)

# this is compare all string
# text='python'
# result=re.fullmatch('python',text)
# print(result)


# advance regex

# using dot

# text='cat caat cet c8t c000t cssdgt'
# result=re.findall('c.t',text)
# print(result)


# string start on this text  using caret
# text='python is awesome'
# Resoult=re.findall('^python',text)
# print(Resoult)


# end of string usign doller sing
# text='i love python '
# result=re.findall('python$',text)
# print(result)


# * using zaro and more
# text='ab abbb abbb a abbb aaab '
# result=re.findall('ab*',text)
# print(result)

# * using one
# text='ab abbb abbb a abbb aaab '
# result=re.findall('ab+',text)
# print(result)

# Question Mark (?)

# text='ab abbb abbb a abbb aaab abbbbbb '
# result=re.findall('ab?b',text)
# print(result)


# 
# text='Apple mango cat bat 123'
# result=re.findall("[abc]",text)
# result=re.findall("[a-z]",text)
# result=re.findall("[A-Z]",text)
# result=re.findall("[1-9]",text)
# print(result)

# text='Apple mango cat bat 123'
# result=re.findall("[^1=9]",text)
# print(result)


# 
# result=re.findall(r"\d",'abc123')
# result=re.findall(r"\D",'abc123') 'digit is not present
# print(result)

# result=re.findall(r"\W",'abc123')# 'char is not present
# print(result)

# tex='i love python 123'
# result=re.findall(r"\S", tex)# 'whitespace k alava
# print(result)



# import re

# text = "I like Java"

# print(re.sub("Java", "Python", text))


# import re

# text = "apple,banana,orange"
# print(re.split(",", text))

# import re

# email = "abc@gmail.com"

# pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# print(bool(re.match(pattern, email)))


# import re

# text = "Call me on 9876543210"

# print(re.findall(r"\d{10}", text))











