# 随机分红包 一共加起来就是10元 8个分
# 多少个每个多少钱
# 谁是最大的
#求和10元 随机的  8次分完  最大的
#random
a={}
import random
print('发的人数')
renshu=int(input())
print('发的钱')
fadeqina=float(input(''))
r=0 #每次随机的钱
s=0 #这个是承接每次发的钱 因为我要用发的钱减去这个s 缩小随机的范围
k=fadeqina*0.01
for i in range(1,renshu+1):
    sk = fadeqina - s
    r=round(random.uniform(0.1, k*sk),2)
    a[f'{i}'] = r
    s += r

print(a)


