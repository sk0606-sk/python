import random

i = 0
c = 4
a = random.randint(1, 10)
while i < 5:

    b = int(input('输入一个整数'))
    if b > a:
        print('很遗憾，你猜大了')
    elif b < a:
        print('很遗憾，你猜小了')
    else:
        print('恭喜成功')
        break
    i += 1
    print()
    print(f'剩余次数{c}')

    c -= 1
    print(f'随机数大小{a}')
    print()
