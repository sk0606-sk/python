i = 0
count = 5
while i < 5:
    j = 0
    while j < i + count:
        print('*', end='')
        j += 1
    i += 1
    count -= 1
    print()
