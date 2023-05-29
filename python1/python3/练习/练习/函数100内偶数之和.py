#创建一个函数一个形参
def oushuhe(a):
    #要遍历出从1到a然后相加 要有一个数来承接和
    sum=0
    for i in range(1,a+1):
        if i %2==0:
            sum+=i
    return sum
print(oushuhe(100))