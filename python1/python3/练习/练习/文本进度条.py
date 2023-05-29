import time

print('==' * 25, end='')
print('开始下载', end='')
print('==' * 25, end='')
print()
for i in range(1, 101):
    print('\r' + f'{i}' + '%' + '[' + '*' * i, end='' + '.' * (100 - i) + ']')
    time.sleep(0.1)
if i == 100:
    print()
    print('==' * 25, end='')
    print('下载完成', end='')
    print('==' * 25, end='')
