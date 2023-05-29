print(f'下载选择y或Y,不下载点击n或N')
cz = input('只能选择y或Y，n或N')
if cz == 'Y' or cz == 'y':
    print(f'下载任务')
else:
    print(f'不下载任务')
    if cz != 'Y' and 'y' and cz != 'n' and 'N':
        print('错误')
