# j=0
# while j<5 :
#     i = 0
#     while i < 5:
#         print("*", end='')
#         i += 1
#     j += 1
#     print()
j = 0
while j < 5:  # 外层循环控制高
    j += 1
    i = 0
    while i < 5:  # 内存循环控制宽 内存循环执行次数等于j*i次
        print('*', end='')
        i += 1
    print()  # 换行
