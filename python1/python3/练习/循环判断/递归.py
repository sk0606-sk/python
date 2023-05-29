# def sk (n):
#     if n==1:
#         return 1
#     else:
#         return n*sk(n-1)
# print(sk(5))
# #假设-段楼梯共15个台阶，小明-步最多能上3个台阶。编写程序计算小明上:这段楼梯一共有多少种方法。要求给出递推法和递归法两种代码。
#
# #递归法
# def demo(n):
#     if n==1 or n==2 or n==3:
#         return 1
#     else:
#         return demo(n-1)+demo(n-2)+demo(n-3)
# print(demo(15))
# 有一群猴子，去摘了一堆桃子，商量之后决定每天吃剩余桃子的一半。可是当每天大家吃完桃子之后，有个贪心的小猴都会偷偷再吃一个桃子。
# 按照这样的方式猴子们每天都快乐的吃着桃子，直到第十天，当大家再想吃桃子时，发现只剩下一个桃子了。
# 问：猴子们一共摘了多少桃子？
# 要求 1.使用递归思想编程
# 2. 提供代码截图和运行结果截图
# 3.运行结果要由“猴子们一共摘了**个桃子”类似的语句组成
def chichi(day,tanchi):
    if day==1:
        return tanchi
    else:
        return chichi(day-1,(day*2+tanchi))
print(chichi(10,1))


