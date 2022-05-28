name = 'jhonsmith'
age = 20
is_new = True
nameInpt=input("Enter your name  ")
ageInpt = input("enter your age ")
if name != nameInpt and age != ageInpt:
    is_new = True
else:
    is_new = False

if is_new:
    print("new")
else:
    print('old')