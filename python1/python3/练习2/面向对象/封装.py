# class ren:
#     def __init__(self,name,age):
#         self.snnnn=name
#         self.ssssss=age
#     def sehhl(self):
#         print(f'大家好晚上，ws {self.snnnn}')
#     def get_name(self):
#         return self.snnnn
#     def get_age(self):
#         return self.ssssss
#     def set_name(self,name):
#         self.snnnn=name
#     def set_age(self,age):
#         self.ssssss=age   #这种封装就是不把属性的真正名字告诉使用者 要调用相关属性调用其get_属性名相关方法 改变其属性一样的调用方法
# sk=ren('sk',18)
# # sk.nnn='skk'
# # print(sk.set_name('xiaog'))
# # print(sk.get_name())
# # print(sk.nnn)
# # sk.sehhl()
# print(sk.get_age())
# sk.set_age(20)
# print(sk.get_age())
class ren:

    def __init__(self,name):
        self.__name=name

    @property
    def get_name(self):
        return self.__name
    
s=ren('sk')
print(s.get_name)
 #__属性名 相当于_类名__属性名'