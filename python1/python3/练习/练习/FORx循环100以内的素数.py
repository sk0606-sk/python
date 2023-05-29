for i in range(2,101):
    falg = True
    for x in range(2,i):
        if i % x == 0:
            falg = False
    if falg:                    #用一个布尔值来代替判断结果 两个数判断被除数不能等于除数这样就解决了一个条件（任何数都能被自己整除）然后被除数递增到结束完都没有被
                                #整除那这个数就是质数最小的因数除了本身一定是这个数的两倍
        print(i)



a=dict()
a['sk']='l'
print(type(a))
print(a)
a.update(sk='lllll')
print(a)
a.setdefault('skkk','dakjdakda')
print(a)
a.pop('sk')
print(a)
a.setdefault('skl','dakjdaa')
a.setdefault('kkk','dakjdakda')
print(a.items())
