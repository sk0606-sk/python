import os
os.chdir(r'C:\sk')
print('输入目录名')
mz = input()
a = os.path.exists(mz)
if a is False:
    cj = os.mkdir(mz)
    print('创建成功')
    print(os.listdir())
else:
    os.chdir(rf'C:\sk\{mz}')
    print('请输入文件名')
    lieb = os.listdir()
    wenjianm = input()
    if wenjianm in lieb:
        print(f'文件在{mz}里')
    else:
        print('文件不在')
