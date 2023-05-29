zhanghao='sk'
mima='123456'
sp=list()
print('请输入账号')
zh = input()
print('请输入密码')
mm = input()
if zh == zhanghao and mm == mima:
    print('登录成功')
    n=1
    while True:
        zd = dict()
        print('''
1.添加商品信息
2.查看商品信息列表
3.修改指定商品
4.删除指定商品
5.退出系统
    ''')
        print('请选择')
        xz = input()
        if xz == '1':
            add_bh = f'c0{n}'
            print('名称')
            add_name = input('')
            print('数量')
            add_sl = int(input())
            print('价格')
            add_jg = int(input())
            zd['编号'] = add_bh
            zd['名称'] = add_name
            zd['数量'] = add_sl
            zd['价格'] = add_jg
            zd['金额']=add_sl*add_jg
            sp.append(zd)
            print('添加成功')
            print(sp)
            n+=1
        elif xz == '2':
            if len(sp)!=0:
                print('-'*30)
                print()
                print('编号\t',end='')
                print('名称\t', end='')
                print('数量\t', end='')
                print('价格\t', end='')
                print('金额\t', end='')
                print()
                print('-' * 30)
                for i in sp:
                    for x in i.values():
                        print(f'{x}\t',end='')
                    print()
            else:
                print('请先添加列表')
        elif xz == '3':
            if len(sp)!=0:
                print('-' * 30)
                print()
                print('编号\t', end='')
                print('名称\t', end='')
                print('数量\t', end='')
                print('价格\t', end='')
                print('金额\t', end='')
                print()
                print('-' * 30)
                for i in sp:
                    for x in i.values():
                        print(f'{x}\t', end='')
                    print()
                xh=input('请输入商品的编号 ')
                for i in sp:
                    if xh in i.values() :
                        k={}
                        xp=sp.index(i)

                        print('数量')
                        add_sl1 = int(input())
                        print('价格')
                        add_jg1 = int(input())
                        zd = add_sl1 * add_jg1
                        k=sp[xp]
                        k.update(数量=add_sl1,价格=add_jg1,金额=zd)
                        print('修改成功')
                        print(sp)
                        break
                    else:
                        print(xh,'buzai')


            else :
                print('请先添加商品')
        elif xz == '4':
            if len(sp)!=0:
                print('-' * 30)
                print()
                print('编号\t', end='')
                print('名称\t', end='')
                print('数量\t', end='')
                print('价格\t', end='')
                print('金额\t', end='')
                print()
                print('-' * 30)
                for i in sp:
                    for x in i.values():
                        print(f'{x}\t', end='')
                    print()
                print('请输入要删除的商品')
                ph=input()
                for i in sp :
                    if ph in i.values():
                        xp=sp.index(i)
                        print('是否删除y/yse/YES，取消操作输入任意内容')
                        xz=input()
                        if xz== 'y' or xz == 'yes' or xz == 'YES':
                            sp.pop(xp)
                        else:
                            print('不删除')

                    else:
                        print(ph, '不在')

            else:
                print('先添加')

        elif xz == '5':
            print('是否要退出，退出:y/yse/YES，取消操作输入任意内容')
            xz1 = input()
            if xz1 == 'y' or xz1 == 'yes' or xz1 == 'YES':
                print('退出成功')
                break
            else:
                print('请重新选择')

        else:
            print('选择有误')
else:
    print('登录失败')

