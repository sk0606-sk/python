nub = int(input('请输入比1大的数：'))
i = 2
flag = True
while i < nub:
    if i % nub == 0:
        flag = False
    i += 1
if flag:
    print("是质数")
else:
    print('不是质数')
