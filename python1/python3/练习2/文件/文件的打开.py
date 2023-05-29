# try:
#     wenjian='sk.txt'
#     with open(wenjian,encoding='utf-8') as sk :  #两个参数 一个打开文件 另一个参数自定义 with open 。。。as 可以把文件操作放在一个里面执行 并且会自动关闭
#         print(sk.read())
# except FileNotFoundError:
#     print(wenjian,'不存在')
try:
    wenjian = 'sk.txt'
    with open(wenjian, encoding='utf-8') as sk:  # 两个参数 一个打开文件 另一个参数自定义 with open 。。。as 可以把文件操作放在一个里面执行 并且会自动关闭
        skk = 100
        neirou = ''
        while True:
            du = sk.read(100)
            if not du:
                break
            neirou += du
            print(du)
except FileNotFoundError:
    print(wenjian, '不存在')
