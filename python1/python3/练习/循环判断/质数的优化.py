from time import *  # 调用一个函数

begin = time()  # 用来计算时间
i = 2
while i <= 100:
    falg = True
    j = 2
    while i > j ** 0.5:
        if i % j == 0:
            falg = False
            break  # 当100除以2能被整除
            # 说明这个数已经不是质数 但是循环条件i>j还是可以满足 那么这个循环还是会true继续执行 所有可以用一个break跳出循环
        j += 1
    if falg:
        print(i)
    i += 1
end = time()
print('时间', end - begin)
