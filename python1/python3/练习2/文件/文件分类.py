import os
import shutil

print('请输入要分类文件的路径')
lj = input()  # C:\Users\商康\Desktop\2023上半年上课资料
try:
    zhuan = os.chdir(rf'{lj}')
    print('创建文件夹.docx')
    shuru = input()
    zbz = os.path.exists(shuru)
    if zbz is True:
        print('文件夹已存在重新创建')
    else:
        lieb = os.listdir()
        print(lieb)
        cj = os.mkdir(shuru)
        for i in lieb:
            x = i.rfind('.')
            hocuim = i[x + 1:]
            if hocuim == 'docx':
                shutil.move(f'{i}', f'{shuru}')
        lieb2 = os.listdir()
        print(lieb2)
        print('创建xlsx的文件夹')
        shu = input()
        zbz2 = os.path.exists(shu)
        if zbz2 is True:
            print('文件夹已存在重新创建')

        else:
            cj2 = os.mkdir(shu)
            for i in lieb2:
                x = i.rfind('.')
                hocuim = i[x + 1:]
                if hocuim == 'xlsx':
                    shutil.move(f'{i}', f'{shu}')
        lieb3 = os.listdir()
        print(lieb3)
        print('创建其他的文件夹')
        shu1 = input()
        zbz3 = os.path.exists(shu1)
        if zbz3 is True:
            print('文件夹已存在重新创建')
        else:
            cj2 = os.mkdir(shu1)
            for i in lieb3:
                x = i.rfind('.')
                hocuim = i[x + 1:]
                if hocuim != 'xlsx' and hocuim != 'docx':
                    shutil.move(f'{i}', f'{shu1}')
except FileNotFoundError:
    print('路径不存在请检查')
