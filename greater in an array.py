print("enter how many numbers")
n =int(input())
i = 0
while i < n:
    list[i]= int(input())
big = list[0]
for i in list:
    if big < i:
        big = i
print(big)
