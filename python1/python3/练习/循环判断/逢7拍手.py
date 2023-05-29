i = 7
for i in range(1, 101):
    g = i % 10
    shi = i // 10
    if i % 7 == 0:
        print(i)
    elif g == 7:
        print(i)
    elif shi == 7:
        print(i)
