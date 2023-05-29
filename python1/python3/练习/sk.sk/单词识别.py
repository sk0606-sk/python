a = dict(mo='Monday', tu='Tuesday', we='Wednesday', th='Thursday', fi='Friday', sa='Saturday', su='Sunday')
b = dict(mon='Monday', tue='Tuesday', wed='Wednesday', thu='Thursday', fri='Friday', sat='Saturday', sun='Sunday')
c = input('请输入简写类似mo或者mon ')
if c in a:
    print(a[c])
elif c in b:
    print(b[c])
else:
    print('输入有误')
