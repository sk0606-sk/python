# 定义一个空列表
a = []
while True:
    print('请输入数字')
    print('如果要退出请输入退出')
    s = input('')
    a.append(s)
    if s == '退出':
        b = a.pop(-1)
        break
for i in a:
    s = int(i)
sum = 0
sum += s
print(sum)
