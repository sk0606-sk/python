zd = dict()
def zid():
    print('输入姓名')
    name = input()
    print('请输入电话')
    number = input()
    print('请输入QQ')
    qq = input()
    print('请输入邮箱')
    youxiang = input()
    if name not in zd:
        zd[f"{name}"] = f'{number},{qq},{youxiang}'
        with open(r'666.txt', 'w', encoding='utf-8') as sk:
            for i in zd.items():
                s1 = "_".join(i)
                # zd1 = str(i)
                sk.writelines(f"{s1}")
    else:
        print(name, '已存在请重新输入')
def shanchu():
    print(zd)
    print('请输入要删除的人')
    ren = input()
    if ren in zd:
        zd.pop(ren)
    else:
        print(ren, '不在通讯录')
    with open('666.txt', 'w', encoding='utf-8') as sk:
        sk.seek(0)
        sk.truncate(0)
        for i in zd.items():
            s1 = "_".join(i)
            sk.writelines(s1)


def du():
    # with open('666.txt', 'r', encoding='utf-8') as sk:
    #     lieb = sk.readlines()
    #     print(lieb)
    #     print('请输入要查找的人')
    #     ren = input()
    #
    #     if ren in lieb:
    #         print(lieb[ren])
    #     else:
    #         print('不在')
    print(zd)
    print('请输入要查找的人')
    ren = input()
    if ren in zd :
        print('电话 qq 邮箱:')
        print(zd[ren])

    else:
        print('不在')

def gai():
    print(zd)
    print('请输入要修改的人')
    ren = input()
    if ren in zd:
        print('请输入电话')
        number = input()
        print('请输入QQ')
        qq = input()
        print('请输入邮箱')
        youxiang = input()
        zd[f"{ren}"] = f'{number},{qq},{youxiang}'
    else:
        print(ren, '不在通讯录')
    with open('666.txt', 'w', encoding='utf-8') as sk:
        sk.seek(0)
        sk.truncate(0)
        for i in zd.items():
            s1 = "_".join(i)
            sk.writelines(s1)


def qingd():
    while True:
        print(''' \
    1.进行添加 
    2.删除
    3.查
    4.改
    5.退出
        ''')
        print('请进行选择')
        xz = input()
        if xz == '1':
            zid()
        elif xz == '2':
            shanchu()
        elif xz == '3':
            du()
        elif xz == '4':
            gai()
        elif xz == '5':
            print('确认要退出请选择y/Y/yes/yes 取消按任意键')
            xz = input()
            if xz == 'y' or xz == 'Y' or xz == 'yes' or xz == 'YES':
                print('退出成功')
                break
            else:
                print('已取消')
        else:
            print('选择有误重新选择')


qingd()
