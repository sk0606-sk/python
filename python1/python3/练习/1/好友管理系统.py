print('='*20,'欢迎使用好友系统','='*20)
print()
hy=[]
while True :
    print('''\
    1:\t添加好友
    2:\t删除好友
    3:\t修改备注
    4:\t展示好友
    5:\t退出
    ''')
    print('-' * 58)
    print('请选择要做得操作')
    xz=input()
    if xz =='1' :
        print('输入要添加的好友')
        name_hy=input()
        if name_hy in hy:
            print(f'{name_hy}已存在')
        else :
            print(f'{name_hy}'"是否添加好友，y/yse/YSE，取消操作输入任意内容")
            xz1 = input('请输入 ')
            if xz1 == 'y' or xz1 == 'Y' or xz1 == 'yse' or xz1 == 'YSE':
                hy.append(name_hy)
                print('添加成功')
            else:
                print('取消成功')
    elif xz =='2' :
        if hy == []:
            print('好友列表为空')
        else :
            print('输入要删的序号')
            cd = len(hy)
            xh = int(input())
            if 0 <= xh <= cd:
                idnex = xh - 1
                print(hy[idnex], '是否删除，删除不可逆，y/yse/YSE，取消操作输入任意内容')
                xz2 = input('请输入 ')
                if xz2 == 'y' or xz2 == 'Y' or xz2 == 'yse' or xz2 == 'YSE':
                    hy.pop(idnex)
                    print('删除成功')
                else:
                    print('删除取消')
    elif xz =='3' :
        if hy==[] :
            print('好友列表为空')
        else :
            cd1 = len(hy) - 1
            name_hy1 = input('请输入要修改的好友名字 ')
            if name_hy1 not in hy:
                print(f'{name_hy1}不是好友')
            elif name_hy1 in hy:
                s = hy.index(name_hy1)
                if 0 <= cd1 and cd1 <= cd1:
                    print(hy[s], '是否修改备注，y/yse/YSE，取消操作输入任意内容')
                    xz3 = input('请输入 ')
                    if xz3 == 'y' or xz3 == 'Y' or xz3 == 'yse' or xz3 == 'YSE':
                        hy[s] = input('请输入要修改的备注')
                        print('备注成功')
                    else:
                        print('取消操作')
                else:
                    print('输入有误，没有改好友 请输入4查看')

    elif xz =='4' :
        if hy==[] :
            print('好友列表为空')
        else :
            i=0
            print('序号\t名字')
            for hy2 in hy :
                i+=1
                print(f'{i}\t{hy2}')
    elif xz =='5' :
        print('退出成功')
        break
    else:
        print('输入有误，重新输入')
