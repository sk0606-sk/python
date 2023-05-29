# # 二、高阶函数
# # -高阶函数至少要符合以下两个特点中的一个
# # 1、接收一个或多个函数作为参数
# # 2、将函数作为返回值返回
# # 接收函数作为参数，或者将函数作为返回值的函数是高阶函数
# l=[1,2,3,4,5,6,7,8,9,10]
# def fn2(i):
#     if i % 2 == 0:
#         return True  # True的意思就是这个数满足这个条件 它是偶数做个印记1 满足条件
#     return False  # 返回一个结果 函数只是做某个功能的代码块
# def fn3(i):  # 函数的形惨就像变量一样 写几个形参 函数内就可以直接使用这几个变量
#     if i > 5:
#         return True
#     return False
# def fn(fun,list):
#     new_list=[]
#     for n in list :
#         if fun(n):
#             new_list.append(n)
#     return new_list
# print(fn(fn2,l))   #fn 是表示一个函数 fn()是调用一个函数必须要有实参 高阶函数是把函数作为实参
#                     #以前都是以具体的字符串值作为实参 现在是以函数 具体的代码块作为参数 因为函数可以做一些功能操作
                    #所有说高阶函数就是以函数作为参数或者以函数作为返回值
                    #到底什么是返回值 返回结果 就是做完这个操作我要什么结果 就返回什么结果 怎么得到返回值 函数怎么使用？print（fn（））得到返回值
                    #递归函数就是 函数自己内部调用自己 有一个基线条件一个递归条件 基线条件就是不能再分下去的哪一个条件 递归就是怎么细分下去的那个操作

# print(list(filter(fn2,l))) #可以理解成filter过滤器 直接就是用函数去直接去处理数据 类似就是直接把l当作一个实参 然后返回一个结果
#  #lambda就是一个创建一个简单函数的方法 第一处是参数，第二处就是返回值 很快捷的创建简单的函数相当于def
# r=lambda a,b:a+b
# print(r(10,20))
# s=list(filter(lambda i:i%3==0,l)) #lambda做的一个操作就是满足i%3==0返回的结果就是Ture 然后filter的两个参数是lambda和l l直接作为一个参数进入lambda满足条件的返回
# print(s)
#
# k=list(map(lambda i:i+1,l)) #map(对可迭代对象所有元素要进行的操作,可迭代对象)
# print(k)
# def fn():
#     def inner():
#         print('ws222')   #另一种高阶函数把函数作为返回值返回
#     return inner
# fn()       #fn（）的返回值是一个函数 所有现在的fn（）就是一个函数
# fn()()     #调用一下fn（）就是打印出print

def pingjun_zhi():
    nums = []
    def sk(a):
        nums.append(a)
        return sum(nums)/len(nums)
    return sk
r=pingjun_zhi()
print(r(10))  #返回值要打印才能看到  闭包就是函数的嵌套 局部函数的变量 可以被某个函数单独使用
                #可以保证数据的私密  内部函数一定要使用外部函数的变量

