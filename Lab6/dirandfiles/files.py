import os

#1

first_dir = os.listdir()
for x in first_dir:
    if os.path.isdir(x):
        first_dir += os.listdir(x)
print(first_dir)

#2

path_dir = "dir/readme"

if os.path.exists(path_dir):
    print(True)
else:
    print(False)
if os.access("dir/readme", os.R_OK):
    print(True)
else:
    print(False)
if os.access("dir/readme", os.W_OK):
    print(True)
else:
    print(False)
if os.access("dir/readme", os.X_OK):
    print(True)
else:
    print(False)

#3

path_input = input("")

if os.path.exists(path_input):
    print(os.listdir(path_input))
else:
    print("Doesn't exist")

#4

file_path = "dir\\folder1\\folder1.1.txt"
file = open(file_path, 'r')
text = file.read()
words = text.split(' ')
print(len(words))

#5

list1 = ["My", "name", "is", "Yernar"]
file_path = "dir\\folder1\\folder1,1\\3.txt"
file = open(file_path, 'w')
for s in list1:
    file.write(s + " ")

#6

letter = 65
for x in range(26):
    file = open("26/" + chr(letter) + ".txt", 'x')
    letter += 1

#7

# Copy information from 1.txt to 2.txt:
path1, path2 = "dir\\1.txt", "dir\\2.txt"
file1 = open(path1, 'r')
file2 = open(path2, 'a')
text = file1.read()
file2.write(text)
file2.close()

#8

# We will delete the file "README.md"
file_path = "C:\\Users\\Ernar\\Desktop\\LabsPP2\\pp2\\Lab6\\dirandfiles\\dir\\readme\\README.md"
if os.access(file_path, os.F_OK):
    print("The path exists")
    os.remove("dir\\readme\\README.md")
else:
    print("The path doesn't exists")