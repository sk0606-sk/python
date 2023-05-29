# l=['aaa','ddd','asd','asdad']
# l.sort(key=len)  #sort的用法 sort（key，reverser）它直接改变原来的列表
# print(l)
# ll=[1,2,3,4,5,6,'10','9']
# print(sorted(ll,key=int,reverse=True)) #它没有直接改变原来的列表  这个函数的返回值是直接返回一个新的列表
# print(ll)
# a=123
# a=int(a)
# a=False
# a='a'-'b'
# print(a)
# sk={}
# sk.setdefault('sk',123)
# sk.setdefault('sk',110)
# sk.setdefault('hello',110)
# sk.update(name='skkk')
# sk['lll']='sksksk'
# print(sk['sk'])
# print(sk)
# d={}
#
# print(sk.copy())
def sk(*,c,b,a):   #不定长参数*后只能接关键字参数 打包成一个元组
    print(c)
# sk(a=10,2,0,30,40,50)   关键字参数只能在关键字参数后
sk(c=10,b=20,a=50)

# 位置参数不能跟在关键字参数后面


def skk(**a):  #**只接受关键字参数 打包成一个字典
    print(a)
skk(a=10)