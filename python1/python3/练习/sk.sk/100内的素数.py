i = 2
while i < 100:
    j = 2
    flag = True
    while i > j:
        if i % j == 0:
            flag = False
        j += 1
    if flag:
        print(i)
    i += 1
