'''
1.输入一个字符串
2.量出长度
3创建一个空的列表来承接切片的
'''


print('输入字符串')
a= list(input())
b=a
cd = len(a)
while cd > 1 or cd==1:
    if cd == 1:
        print(b, '是回文字符串')
        break
    elif a[0] != a[-1] :
        print(b, '不是回文字符串')
        break
    elif a[0] == a[-1] :
        a=a[1:-1]
        cd = len(a)
        if cd ==2 :
            if a[0]==a[-1]:
                print(b,'是回文数')
                break

