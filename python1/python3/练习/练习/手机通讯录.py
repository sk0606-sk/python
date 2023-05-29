# update 添加键值对
# add_dict={'name':'小米'}
# add_dict.update(age='18')
# add_dict['address']='nx'
# print(add_dict)
# # update修改键值对
# add_dict.update(age='20')
# add_dict['address']='ZZ'
# print(add_dict)
# add_dict.pop('name')
# add_dict.popitem()
# add_dict.clear()
# print(add_dict)
print('=' * 30)
txl = dict()
while True:
    print('''' 
    1.添加练习人
    2.查看通讯录
    3.删除联系人
    4.修改练习人
    5.查找联系人
    6.退出
    ''')
    print('请输入1-6')
    xz = int(input(''))
    if xz == 1:
        print('请输入联系人姓名')
        name = input()
        print('请输入联系人的手机号')
        num = input()
        print(f'是否添加 {name} 电话号码为 {num} 进入通讯录', 'y/yse/YES，取消操作输入任意内容')
        xz1 = input()
        if xz1 == 'y' or xz1 == 'yes' or xz1 == 'YES':
            txl[name] = num
            print('添加成功')
        else:
            print('取消操作')
    elif xz == 2:
        if txl == {}:
            print('通讯录无信息')
        else:
            print('  姓名\t', '\t电话')
            for i in txl.items():
                print(f'{i}\t')
    elif xz == 3:
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
    elif xz == 4:
        pass
    elif xz == 5:
        print('姓名')
        for x in txl.keys():
            print(x)
    else:
        pass
