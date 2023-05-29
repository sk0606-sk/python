zd={}

def cha_kan():
    if len(zd)!=0:
        for i,v in zd.items() :
            print('英文\t  中文')
            print(i,v,end='')
        print()
    else:
        print('生词本内容为空')
def beican_ci():
    if len(zd)==0:
        print('单词本为空')
    else:
        for i in zd.keys():
            print('英文\t,中文')
            print(i, end='')
        print()
        print('请背单词')
        danci = input()
        if danci in i:
            print(i)
            s = zd[i]
            print('请输入翻译')
            fanyi = input()
            if fanyi == s:
                print('太棒了')
            else:
                print('再想想')
def tianjia_danci():
    print('请输入单词')
    add_canci=input()
    print('请输入翻译')
    add_fanyi1=input()
    if add_canci in zd:
        print('单词已在生词本')
    else:
        zd.setdefault(add_canci,add_fanyi1)
        print('单词添加成功')
def shanchu_danci():
    for i,v in zd.items():
        print('')
        print(i,v,end='')
    print()
    print('请输入要删除的单词')
    sahnchu_canci=input()
    if sahnchu_canci not in zd:
        print(sahnchu_canci,'不在单词列表')
    else :
        zd.pop(sahnchu_canci)
        print('删除成功')
def qingk():
    if len(zd)==0:
        print('生词本为空')
    else:
        print('是否要请空操作不可以请做出选择y/Y/yse/YES，取消操作输入任意内容')
        xz=input()
        if xz == 'y' or xz == 'yes' or xz == 'YES':
            zd.clear()
        else:
            print('取消操作')


def xz():
    while True:
        print('''
1.查看生词表
2.背单词
3.添加新单词
4.删除单词
5.清空单词表
6.退出单词
  ''')
        print('请选择')
        xz = input()
        if xz == '1':
            cha_kan()
        elif xz == '2':
            beican_ci()
        elif xz == '3':
            tianjia_danci()
        elif xz == '4':
            shanchu_danci()
        elif xz == '5':
            qingk()
        elif xz == '6':
            print('是否要退出操作不可以请做出选择y/yse/YES，取消操作输入任意内容')
            xz = input()
            if xz == 'y' or xz == 'Y' or xz == 'yes' or xz == 'YES':
                print('退出成功')
                break
            else:
                print('取消操作')
        else:
            print('有误')

xz()





