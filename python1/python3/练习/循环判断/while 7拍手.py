i = 0
count = 0
while i < 100:
    i += 1
    g = i % 10
    shi = i // 10
    if i % 7 == 0 or g == 7 or shi == 7:
        print(i, end=' ')
        count += 1
        if count % 10 == 0:
            print()

# 一行打印十个
