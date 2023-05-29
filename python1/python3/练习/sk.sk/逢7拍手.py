for i in range(1, 101):
    g = i % 10
    s = i // 10
    if i % 7 == 0:
        print(i)
    elif g == 7 or s == 7:
        print(i)
