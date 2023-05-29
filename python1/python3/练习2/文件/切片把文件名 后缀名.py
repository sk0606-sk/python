print('输入文件名')
a = input('')
cd = len(a)
for i in range(cd):
    x = a.rfind('.')
    if a[i] == '.':
        wenjianm = a[0:x]
        hocuim = a[x + 1:]
        print(f'文件名为{wenjianm}', f'后缀名{hocuim}')
        break
