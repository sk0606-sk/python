yera = int(input('请输入年份 '))
month = int(input('请输入月份 '))
if month in [1, 5, 7, 8, 10, 12]:
    print(f'{yera}年的{month}月 有31天')
elif month in [4, 6, 9, 11]:
    print(f'{yera}年的{month}月 有30天')
elif month == 2:
    if yera % 400 == 0 or (yera % 4 == 0 and yera % 100 != 0):
        print(f'{yera}年的{month}月 有29天')
    else:
        print(f'{yera}年的{month}有28天')
