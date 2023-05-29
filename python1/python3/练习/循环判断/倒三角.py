# ***** j 5  0  0 5
# ****    4  1  3
# ***     3  2  1
# **      2  3  -1
# *       1  4  -3
# i=0
# while  i< 5:
#     j=5
#     while j <i-j:
#         print('*',end='')
#         j += 1
#         print()
# i+=1
# i=0
# while i<5:
#     j=0
#     while j<j+5:
#         print('*',end='')
#         j+=1
#     i += 1
#     print()
# i = 1 # 预先规定行数
# while i < 6: # 设定条件1，以保证行数为5，在第六行i=0停止运行
#     j = 1 # 给变量j赋值为0
#     while j < 7-i : # 规定条件2，以保证每一行*的数量与行数相同
#         print("*",end="\t") # \t 为ASCII水平制表符，end=""是为了不让代码自动换行
#         j +=1 # 使每一行的*的数量增长
#     print("") # 让每一行换到下一行
#     i += 1 #  使行数不断地增长
j = 1
h = 4
while j < 6:
    i = 0
    while i < j + h:
        print('* ', end='')
        i += 1
    j += 1
    h -= 2
    print()
