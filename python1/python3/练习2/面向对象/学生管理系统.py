xuesheng = []
zidian = dict()
class xs:
    def zengjia(self):
        print('请输入学生姓名')
        xm=input()
        print('请输入学生的年龄')
        age=input()
        print('请输入学生的性别')
        xb=input()
        zidian[f"{xm}"]=f'{xb,age}'
        xuesheng.append(zidian)
    def chazhao(self):
        if xuesheng==[]:
            print('学会系统为空')
        else:
            print(xuesheng)
            print('请输入要查找人的姓名')
            cz=input()
            for i in xuesheng :
                if cz in i :
                    print(i[cz])
                else:
                    print(cz,'不在学生系统中')
    def xiugai(self):
        if xuesheng == []:
            print('學生系統爲空')
        else:
            print('请输入要修改的学生')
            xues = input()
            for i in xuesheng:
                if xues in i:
                    print('请输入要修改的年龄')
                    age = input()
                    print('请输入要修改的性别')
                    xingb = input()
                    i[xues] = f'{age},{xingb}'
                else:
                    print(xues, '不在改系统')
    def shanchu(self):
        if xuesheng == []:
            print('學生系統爲空')
        else:
            print('请输入要修改的学生')
            xues = input()
            for i in xuesheng:
                if xues in i:
                    print('请输入要删除的姓名')
                    xue=input()
                    for i in xuesheng:
                        if xues in i:
                            i.pop(xues)
                        else:
                            print('此生不在该系统')
    def xuez(self):
        while True:
            print('''\
            1:\t增加学生信息
            2:\t查找学生信息
            3:\t修改学生信息
            4:\t删除学生信息
            5:\t退出
            ''')
            print('-' * 58)
            print('请选择要做得操作')
            xz = input()
            if xz == '1':
                xs.zengjia(self)
            elif xz == '2':
                xs.chazhao(self)
            elif xz == '3':
                xs.xiugai(self)
            elif xz == '4':
                xs.shanchu(self)
            elif xz == '5':
                print('确定要退出请输入y Y yes YES 取消请按任意键')
                xz = input()
                if xz == 'Y' or xz == 'y' or xz == 'yes' or xz == 'YES':
                    print('成功退出')
                    break
            else:
                print('输入有误重新输入')
xs.xuez('启动')