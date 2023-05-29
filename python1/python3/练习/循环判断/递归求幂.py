# 1.创建一个函数 power 来为任意数字做幂运算 n**i
# 10**5 10**4 *10
# def power(n,i):
#     n**i
#     if i==1:
#         return 1
# #     return n*power(n,i-1)
# # print(power(5,5))
# def power(n,i):
#     if i==1 :
#         return n
#     return n*power(n,i-1)
# print(power(5,3))
import os
with open('new_file.txt','r')as sk:
    print(os.access('new_file.txt',os.F_OK))
    print(os.access('new_file.txt', os.R_OK))
    print(os.access('new_file.txt', os.W_OK))
    print(os.access('new_file.txt', os.X_OK))
    print(os.getcwd())
    os.chdir(r'/A:')