year = int(input('请输入年份'))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f'{year}是润年')
else:
    print(f'{year}不是润年')
