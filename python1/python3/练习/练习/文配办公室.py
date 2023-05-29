# import random
# print('老师为1-8号')
# print('办公室为a，b，c')
# bgs=['a','b','c']
# ls=[['1'],['2'],['3'],['4'],['5'],['6'],['7'],['8']]  #来一个嵌套类表 这种列表第一次遍历出的是列表 一层一层剥开
# x=0
# a=0
# b=0
# c=0
# for i in ls :
#     js = random.choice(bgs)
#     ls[x].append(js)
#     x+=1
# print(ls)
# for h in range(len(ls)):
#     l=ls[h][1]
#     if l =='a':
#         a+=1
#     elif l =='b':
#         b+=1
#     else :
#         c+=1
# print(f'办公室人数为{a}')
# print(f'办公室人数为{b}')
# print(f'办公室人数为{c}')
import random
js=[[],[],[]]
ls=[1,2,3,4,5,6,7,8]
for i in ls :
    s=random.randint(0,2)
    js[s].append(i)
print(js)