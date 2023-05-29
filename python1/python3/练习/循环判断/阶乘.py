#输入一个数
#定义一个变量 用来接受乘机
#循环从1到它本身
# print('输入一个整数')
# a=int(input())
# s=a
# for i in range(1,a): #左开右闭 所以要取到a 右闭的范围应该是 a+1
#     s*=i #sum=sum*i    每次相乘的结果赋值给sum
# print(f'阶乘为{s}')
#递归求阶乘

# def sk(a):
#     s = a
#     for i in range(1,s):
#         s*=i
#     if a==1:     #递归就直接在自己这个函数内直接调用自己这个函数 一般都是条件差一利于10！=1*2*3*4*5*6*7*8*7*10
#         return 1  #我就可以直接 来一个n*n-1来求值
#     return a*sk(a-1)
# print(sk(10))
def jie_shneg(a):
    s=a
    for i in range(1,a) :
        s*=i
    if a==1:
        return 1
    return a*jie_shneg(a-1)
print(jie_shneg(10))
