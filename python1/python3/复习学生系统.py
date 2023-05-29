xs=dict(sk='sjsj')
def tj():
    print('请输入联系人的姓名')
    name=input()
    print('请输入联系人de手机号')
    phone=input()
    print('请输入联系人的邮箱')
    youx=input()
    print('请输入联系人de地址')
    address=input()
    # xs.setdefault(name,f"{phone,youx,address}")
    xs[f'{name}']=f'{phone},{youx},{address}'
def chakan():
    if xs == {}:
        print('学生系统为空')
    else:
        print(xs)
        print('请输入要查看的姓名')
        name=input()
        if name in xs.keys():
            print(xs[name])
def shanchu():
    if xs == {}:
        print('学生系统为空')
    else:
        print(xs)
        print('请输入要删除的姓名')
        name = input()
        if name in xs.keys():
            xs.pop(name)
        else:
            print(name,'不在学习系统')
del xs['sk']
a=[1,2,3,6,4,5,9]
del a[1]
a.remove(2)
a.pop(0)
a.clear()
print(xs)