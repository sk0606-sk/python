# class sdada():#都是公共属性 只要是sdada的实例都可以调用
#     name='sk'#
#     #函数在class里变为方法 实例调用方法的时候系统默认会自调用一个位置参数 所有我们在class里定义方法的时候最少要有一个形参
#     def heelo_word(self):
#         print(self.name)
# print(sdada)
# sl=sdada()  #成为sdada的实例
# sll=sdada()
# print(sl,type(sl))
# result=isinstance(sl,sdada) #检查某个对象是不是这个类的所属
# print(result)
# sl.name='sk'
# sll.name='skkk'
# print(sl.name)     #面向对象找属性的顺序是 先找自己有没有该属性没有 去类里面找 类里面没有报错
# sl.heelo_word()     #调用属性的方法就是 xx.属性
# sll.heelo_word()
# class MxdX():
#     print('ssssss')
#     def __init__(self,):
#         print(type(self),id(self))   #魔术方法系统会自动调用   所有类似于 这个类的共同属性  这个形参是每个实例 也就是说 创建的这个属性在实例内
#         #class 的代码块也是从上往下调用
#
#
# p=MxdX()
# p1=MxdX()
# print(id(p))
class Person:
#     a=1      #属性一直在要不要用看自己调不调用
#     def __init__(self,name): #这个魔术方法它默认一定会把变量这个对象传进去 其实它实实在在的功能就是手动传入参数这自动创建属性
#         #魔术方法可以初始化对象的属性 应为它在对象创建的时候自动调用 要怎么样的属性我们可以自定义
#         self.name=name
    def say_hello(self,name):
        print(f'大家好，我是%s'%self.name)
p1=Person()
p1.name='孙悟空'
print(p1.say_hello())
print(p1.a)





# p1.name='孙悟空'
# p2=Person()
# p2.name='猪八戒'
# p3=Person()
# p3.name='沙和尚'
# p3.say_hello()