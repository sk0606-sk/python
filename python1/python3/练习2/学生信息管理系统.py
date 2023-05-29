xuesheng=[]
zidian=dict()
def zengjia():
    print('请输入学生的姓名')
    xingming=input()
    print('请输入学生的年龄')
    age=input()
    print('请输入学生的性别')
    xingbie=input()

    zidian.setdefault(xingming, f"{age},{xingbie}")
    xuesheng.append(zidian)
def chazhao() :
    if xuesheng==[]:
        print('學生系統爲空')
    else:
        print(xuesheng)
        print('请输入查找的学生')
        xues=input()
        for i in xuesheng:
            if xues in i :
                print(i[xues])
            else:
                print(f'{xues}不在改学生系统')
def xiugai():
    if xuesheng==[]:
        print('學生系統爲空')
    else:
        print('请输入要修改的学生')
        xues=input()
        for i in xuesheng:
            if xues in i:
                print('请输入要修改的年龄')
                age = input()
                print('请输入要修改的性别')
                xingb = input()
                i[xues] = f'{age},{xingb}'
            else:
                print(xues,'不在改系统')
def shanchu():
    if xuesheng==[]:
        print('學生系統爲空')
    else:
        print('请输入要删除的学生')
        xues=input()
        for i in xuesheng:
            if xues in i :
                i.pop(xues)
            else:
                print('此生不在该系统')
def xuez():
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
        if xz=='1':
            zengjia()
        elif xz=='2':
            chazhao()
        elif xz=='3':
            xiugai()
        elif xz=='4':
            shanchu()
        elif xz=='5':
            print('确定要退出请输入y Y yes YES 取消请按任意键')
            xz=input()
            if xz =='Y' or xz=='y' or xz=='yes' or xz=='YES':
                print('成功退出')
                break
        else :
            print('输入有误重新输入')
xuez()