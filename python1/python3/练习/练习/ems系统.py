print('=' * 20 + '欢迎使用员工管理系统' + '=' * 20)
yg = [f'\tsk\t19\t男\t花果山', '\tyyx\t19\t女\t花果山']
while True:
    print('请选择要做得操作')
    print('''\
     \t1.查询员工
     \t2.添加员工
     \t3.删除员工
     \t4.退出系统 
     ''')
    print('-' * 58)
    xz = input('请选择1-4= ')
    if xz == '1':
        print('序号\t姓名\t年龄\t性别\t 地址')
        xh = 1
        for emp in yg:
            print(f'{xh}{emp}')
            xh += 1
    elif xz == '2':
        name = input('请输入名字= ')
        age = input('请输入年龄= ')
        ex = input('请输入性名= ')
        address = input('请输入地址= ')
        print(f'{name},{age},{ex},{address} 是否加入系统')
        xz2 = input('请输入y/n ')
        if xz2 == 'y' or xz == 'Y' or xz2 == 'yse' or xz2 == 'YSE':
            yg.append(f'\t{name}\t{age}\t{ex}\t{address}')
            print('-' * 58)
            print('加入成功')
        else:
            print('-' * 58)
            print('取消加入操作')
    elif xz == '3':

        schu = int(input('输入序列号 '))
        if 0 < schu <= len(yg):
            idex = schu - 1
            print('序号 姓名 年龄 性别 地址')
            print(f'{schu}{yg[idex]}')
            print("是否删除，删除不可逆y/n yse/no YSE/NO'")
            xz3 = input('请输入 ')
            if xz3 == 'y' or xz3 == 'Y' or xz3 == 'yse' or xz3 == 'YSE':
                yg.pop(idex)
                print('删除成功')
            else:
                print('删除取消')
    elif xz == '4':
        break
        print('退出成功')
    else:
        print('输入有误')
        break
