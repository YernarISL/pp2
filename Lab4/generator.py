#1

N = int(input("N: ")) 
def squares(N):
    for i in range(1, N + 1):
        yield i * i
obj = squares(N)
for j in range(1, N + 1):
    print(next(obj))

#2

n = int(input("n: "))
def evens(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i
obj = evens(n)
for j in range(0, n // 2 + 1):
    if j < n // 2:
        print(next(obj), end=',')    
    else:
        print(next(obj))

#3

n = int(input("n: "))
def div(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
obj = div(n)
for j in obj:
    print(j)

#4

a, b = int(input("a: ")), int(input("b: "))
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i
obj = squares(a, b)
for x in obj:
    print(x)

#5
    
n = int(input("n: "))
def fromN(n):
    for i in range(n, 0, -1):
        yield i
obj = fromN(n)
for x in obj:
    print(x, end=' ')
