#1
grames = int(input(""))
def convertToOunces(gram):
    ounes = gram * 28.3495231
    return ounes
print(convertToOunces(grames))
#2
F = int(input())
def convertToCent(F):
    C = (5 / 9) * (F - 32)
    return C
print(convertToCent(F))
#3
def solve(numheads, numlegs):
    chickens = numlegs // 4
    rabbits = numheads - chickens
    return chickens, rabbits
print(solve(35, 94))
#6
text = input()
def rev(text):
    new = text.split(' ')
    for i in range(0, len(new)):
        print(new[len(new) - i - 1], end=' ')
rev(text)
#7
nums = list(map(int, input().split()))
def has_33(nums):
    ind = False
    for i in range(len(nums)):
        if nums[i] == 3 and nums[i + 1] == 3:
            ind = True
    if ind:
        return True
    else:
        return False

print(has_33(nums))
#8
nums = list(map(int, input().split()))
def spy_game(nums):
    ind = 0
    check = False
    for i in range(len(nums)):
        if nums[i] == 0 and ind != 2:
            ind += 1
        elif nums[i] == 7 and ind == 2:
            check = True
    if check:
        return True
    else:
        return False
print(spy_game(nums))

