sz = int(input('三位数字 '))
b = (sz // 100) ** 3
s = ((sz % 100 // 10)) ** 3
g = (sz % 10) ** 3
if sz == b + s + g:
    print('是水仙花数')
else:
    print('不是水仙花数')
