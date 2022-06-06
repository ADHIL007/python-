s = 3
i = 0
f = 0
while i < 3:
    c = int(input('Guess your number :'))
    i = i + 1
    if c == s:
        print('you win')
        f = 1
        break


if f == 0:
    print('you lose')


