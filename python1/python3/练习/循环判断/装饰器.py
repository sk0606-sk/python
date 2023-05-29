def fn():
    print('这个代码是我的不能修改')

def fn1():
    print('不能修改吗 那我就调用你然后我自己创建一个我自己的代码进行修改')
    fn()
fn1()

def add(a,b):
    a+b
    return a+b

# def fn2(a,b):
#     print('我要给add增加一个乘法功能')
#     a*b
#     add(a,b)
#     return a*b ,add(a,b)
# print(fn2(10,50))
#这种创建一个新的函数进行拓展工作量太对了 如果 100要拓展那就要创建100个新的函数
#那我们的另一种方法一样也是创建函数但是是自动创建函数
#函数内嵌套一个函数，每调用一次函数就会创建一个函数就相当于每调用一次就会
#重新创建了一个对象 已经解决了自动创建函数那么怎么解决拓展
#被拓展的函数不能写死那么怎么搞 ？
#我们可以在嵌套的函数内 那个内部函数 搞一个变量 这个变量干啥呢
#我们可以把要拓展的函数做为一个参数 传入 这样就没有写死
#如果要拓展的函数有参数怎么搞 那我们可以用不定长参数
def zidongchuangjianhanshu(hanshu):
    '''
    创建一个函数 这个函数的作用就是拓展
    函数内调用要被拓展的函数
    要注意不能写死调用的函数
    需要注意函数参数的问题
    '''
    def tuozhan(*weizhi,**guanjianzi):
        print('开始')
        R=hanshu(*weizhi,**guanjianzi)
        print('结束')
        return R
    return tuozhan
r=zidongchuangjianhanshu(add)
print(r(132,456))

def lll(l):
    def sk(*weizhi, **guanjianzi):
        print('开始')
        R =l(*weizhi, **guanjianzi)
        print('结束')
        return R
    return sk
r=lll(add)
print(r(132,456))

@lll
@zidongchuangjianhanshu    #可以直接用@来代表装饰器  但是要注意的是 @只是一个快捷方式 这个装饰器函数 函数嵌套 不定长参数 函数作为参数 还有返回值
def skl():                  #@可以更简便 就不要把函数作为参数 它直接改造函数 当有多个装饰器的时候 它的装饰循序是从内往外
    print('llll')           #python严格区分大小写 还有缩进 定义变量尽量不要定内置函数的变量 而且有严格的先后的顺序
skl()
