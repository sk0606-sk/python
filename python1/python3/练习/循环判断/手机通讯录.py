print('=' * 30)
txl = dict()
while True:
    print('''
    1.添加练习人
    2.查看通讯录
    3.删除联系人
    4.修改练习人
    5.查找联系人
    6.退出
    ''')
    print('请输入1-6')
    xz = input('')
    if xz == '1':
        print('请输入联系人姓名')
        name = input()
        print('请输入联系人的手机号')
        num = input()
        print('请输入邮箱')
        yx = input()
        print('请输入地址')
        address = input()
        s=len(num)
        if name in txl :
            print(f'{name}已存在通讯录，请检查无误后再添加')
        elif s>11 or s<11:
            print(f'{num}长为{len(num)}不符合电话号码长度，检查后重新输入')
        elif name not in txl and s==11:
            print(f'是否添加 {name} 电话号码为 {num} 进入通讯录', 'y/yse/YES，取消操作输入任意内容')
            print(f'是否添加 邮箱为{yx} 地址为 {address} 进入通讯录')
            xz1 = input()
            if xz1 == 'y' or xz1 == 'yes' or xz1 == 'YES':
                txl[ name] = f'电话 {num},邮箱 {yx},地址 {address}'
                print('添加成功')
            else:
                print('取消操作')
    elif xz == '2':
        if txl == {}:
            print('通讯录无信息')
        else:
            print(txl)
    elif xz == '3':
        if txl == {}:
            print('通讯录无信息')
        else :
            print('请输入要删除的联系人的名字')
            sc = input()
            if sc in txl:
                print(f'是否删除{sc}', 'y/yse/YES，取消操作输入任意内容')
                xz2 = input()
                if xz2 == 'y' or xz2 == 'yes' or xz2 == 'YES':
                    txl.pop(sc)
                    print('删除成功')
                else:
                    print('取消操作')
            else:
                print(f' {sc}不在通讯录内')
    elif xz == '4':
        if txl == {}:
            print('通讯录无信息')
        else :
            print('请输入要修改的姓名')
            name1 = input()
            if name1 in txl:
                print('请输入新联系人的手机号')
                num1 = input()
                print('请新输入邮箱')
                yx1 = input()
                print('请新输入地址')
                address1 = input()
                print('是否要修改，退出:y/yse/YES，取消操作输入任意内容')
                xz4 = input()
                if xz4 == 'y' or xz4 == 'yes' or xz4== 'YES':
                    txl[name1] = f'电话{num1},邮箱{yx1},地址{address1}'
                    print(txl[name1])
            else:
                print(name1, '不在通讯录内')
    elif xz == '5':
        if txl=={}:
            print('通讯录为空')
        else :
            print('请输入要查找的姓名')
            name2=input()
            if name2 in txl:
                print(txl[name2])
            else :
                print(name2,'不在通讯录内')
    elif xz=='6':
        print('是否退出，退出:y/yse/YES，取消操作输入任意内容')
        xz3 = input()
        if xz3 == 'y' or xz3 == 'yes' or xz3 == 'YES':
            print('退出成功')
            break
    else :
        print('选择有误')