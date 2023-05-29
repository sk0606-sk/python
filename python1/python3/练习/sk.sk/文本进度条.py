print('==' * 25, end='')
print('开始下载', end='')
print('==' * 25, end=' ')
print()
import time

for i in range(101):
    print('\r', i, '%' + '[' + f'*' * i, end='' + '.' * (100 - i) + ']')
    time.sleep(0.01)
    if i == 100:
        print()
        print('==' * 25, end='')
        print('下载完成', end='')
        print('==' * 25, end=' ')
# range的范围是一个左闭右开的区间 不设置起始位置是从1开始
# \r相当于一个回车 每次都会返回到行首
# 不同类型的数据不能并接 可以用格式化字符串进行格式化 f''
