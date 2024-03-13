import re

#1

text = input("")
x = re.findall(r"ab*", text)
print(x)

#2

text = input("")
match = re.findall(r"a+b{2}|a+b{3}", text)
print(match)

#3

text = input("")
match = re.findall(r"[a-z]+_+[a-z]*[a-z]", text)
print(match)

#4

text = input("")
match = re.findall(r"[A-Z]{1}[a-z]+", text)
print(match)

#5

text = input("")
match1 = re.findall(r"a.*?b", text)
match2 = re.findall(r"a.*b$", text)
print(match1 + match2)

#6 

text = input("")
match = re.sub(r"[\s.,]",":",text)
print(match)

#8

text = input("")
match = re.findall("[A-Z]*[A-Z]", text)
print(match)