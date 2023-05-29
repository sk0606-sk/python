heads=int(input('一共几个头'))
legs=int(input('一共几条腿'))
for i in range(1,heads+1):
    print('一共有',i,'只鸡')
    print('一共有', heads-i, '只兔子')
    print()
else:
    print('NO answer')
print('余番尤')