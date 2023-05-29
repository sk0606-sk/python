#搞一个字典
#字符串是key
#出现次数是values
zd=dict()
print('输入字符串')
s=input()
for i in s :
    if i in zd :
        zd[i]+=1
    else :
        zd[i]=1
print(zd)
