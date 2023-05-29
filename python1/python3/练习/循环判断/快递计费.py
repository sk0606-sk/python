dq = int(input('输入地区编号01.02.03 '))
zl = float(input('kg '))
if dq == 1:
    if zl <= 2:
        print('快递费13')
    elif zl > 2:
        kdfy = 13 + (zl - 2) * 3
        print(f'{kdfy}元')
elif dq == 2:
    if zl <= 2:
        print('快递费12')
    elif zl > 2:
        kdfy = 12 + (zl - 2) * 2
        print(f'{kdfy}元')
elif dq == 3:
    if zl <= 2:
        print('快递费14')
    elif zl > 2:
        kdfy = 14 + (zl - 2) * 4
        print(f'{kdfy}元')
elif zl > 3:
    print('请找快递员')
