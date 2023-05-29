import random

print('1锤头，2剪刀，3布')
print('假如没有分出胜负请继续进行')
ay = 0
by = 0
dp = 0
guiz = ['锤头', '剪刀', '布']
for i in range(5):
    a = random.choice(guiz)
    b = random.choice(guiz)
    if (a == '锤头' and b == '剪刀') or (a == "剪刀" and b == '布') or (a == '布' and b == '锤头'):
        ay = ay + 1
        if ay == 3:
            print('a赢')
            break
    if (b == '锤头' and a == '剪刀') or (b == "剪刀" and a == '布') or (b == '布' and a == '锤头'):
        by += 1
        if by == 3:
            print('b赢')
            break
    if a == b:
        dp += 1
i += 1
print(f' a赢了{ay}次数, b赢了{by}次数, 打平了{dp}次数')
