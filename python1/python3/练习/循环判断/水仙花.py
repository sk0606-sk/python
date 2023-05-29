# s3 = float(input('输入一个三位数'))
# bai = s3 // 100
# shi = (s3 - bai * 100) // 10
# ge = (s3 - bai * 100) % 10
# bai3 = bai * bai * bai
# shi3 = shi * shi * shi
# ge3 = ge * ge * ge
# if bai3 + shi3 + ge3 == s3:
#     print(f'是水仙花数')
# else:
#     print(f'不是水仙花')

shu=float(input('请输入一个三位数'))
baiwei = shu // 100
shi = shu % 100 // 10
ge = shu % 10
print(baiwei,shi,ge)
if (baiwei ** 3) + (shi ** 3) + (ge ** 3) == shu:
    print(shu, '是水仙花数')
else:
    print(shu, '不是水仙花数')

for i in range(5):
    for x in range(i+1):
        print('*',end="")

    print()
