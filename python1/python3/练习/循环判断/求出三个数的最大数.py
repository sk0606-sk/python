# shu=int[input(),input(),input()]
# for num in shu :
#     print(num[1])


shu1 = int(input())
shu2 = int(input())
shu3 = int(input())
if shu1 > shu2 and shu1 > shu3:
    print(f'{shu1}最大')
elif shu1 < shu2 and shu2 > shu3:
    print(f'{shu2}最大')
else:
    print(f'{shu3}最大')
