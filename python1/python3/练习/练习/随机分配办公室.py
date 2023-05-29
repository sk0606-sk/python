import random

print('假设三个办公室为a,b,c')
print('假设老师为1-8')
a = ['a', 'b', 'c']
# b=[1,2,3,4,5,6,7,8]
c = []
for i in range(1, 9):
    ls = random.choice(a)
    ys = c.append(f'{ls}{i}')
print(c)
