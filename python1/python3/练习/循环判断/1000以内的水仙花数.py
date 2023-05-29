i = 100
while i < 1000:
    b = i // 100
    s = i % 100 // 10
    g = i % 10
    if b ** 3 + s ** 3 + g ** 3 == i:
        print(i)
    i += 1
for i in range(1,1000):
    if i >99:
        b=i//100
        s=i%100//10
        g=i%10
        if b**3+s**3+g**3==i :
            print(i,'是水仙花数')
    else:
        si=i//10
        gi=i%10
        if si**3+gi**3==i:
            print(i,'是水仙花数')

