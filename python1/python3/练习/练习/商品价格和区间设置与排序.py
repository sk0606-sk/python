jg = [399, 4369, 539, 288, 109, 749, 235, 190, 99, 1000]
s2 = int(input('请输入最大的价格:'))
s1 = int(input('请输入最小的价格:'))
px = (input('输入1价格降序，输入2价格升序 '))
px2 = []
for i in jg:
    if s1 <= i and i <= s2:
        px2.append(i)
if px == '1':
    d = sorted(px2, reverse=True)
    print(d)
if px == '2':
    px2.sort()
    print(px2)
