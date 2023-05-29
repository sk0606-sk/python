i = int(input('输入一个数'))
for x in range(2, i):
    if i % x == 0:
        print('不是素数')
        break
else:
    print(f'{i}是素数')
