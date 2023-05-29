import random
chepai=[]
for i in range(20):
    chepai1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','F','Z']
    chepaihao=[0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','F','Z']
    a=random.sample(chepaihao,5)
    a2=" ".join(map(str,a))
    a1=random.choice(chepai1)
    num=f'{i}.京{a1}-{a2}'
    chepai.append(num)
print(chepai)
print('欢迎使用京牌摇号系统')
print('你只有三次机会')
print('请输入要选择的车牌号的循序')
i=3
while i >0:
    xz=int(input())
    if chepai[xz] in chepai:
            i-=1
            print(f'你选择了',chepai[xz])
            print(f'你还有{i}机会')
    else :
        print('输入有误')



