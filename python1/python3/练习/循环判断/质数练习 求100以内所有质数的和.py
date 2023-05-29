# i=2
# while i<=100 :
#     j=2
#     flag =True
#     while j<i :
#         if i%j==0 :
#             flag=False
#         j+=1
#     if flag :
#         print(i)
#     i += 1
# 外层循控制内层循环 外层循环运行一次 内存循环是运行一周

i = 2
while i <= 100:
    falg = True
    j = 2
    while i > j:
        if i % j == 0:
            falg = False
        j += 1
    if falg:
        print(i)
    i += 1
#质数是只能被自己和1整除的数 1既不是质数也不是素数 所有一般我们求质数都是从二开始