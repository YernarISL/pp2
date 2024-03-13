import math

#1

nums = [1, 2, 3, 5, 8, 6, 7]
x = math.prod(nums)
print(x)

#2

string = input("")
lowers, uppers = 0, 0
for x in string:
    if x.islower():
        lowers += 1
    elif x.isupper():
        uppers += 1
print(f"lowers: {lowers} \nuppers: {uppers}")

#3

string = input("")
rev_string = ''.join(reversed(string))
if rev_string == string:
    print(True)
else:
    print(False)

#4

num, mili = int(input()), int(input())
print(f"Square root of {num} after {mili} miliseconds is {math.sqrt(num)}")

#5

x = (True, True, True, True, True, True, True)
if sum(x) == len(x):
    print(True)
else:
    print(False)
    