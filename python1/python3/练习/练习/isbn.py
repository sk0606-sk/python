# 识别码的计算方法如下：
#
# 首位数字乘以1加上次位数字乘以2……以此类推，用所得的结果mod11，所得的余数即为识别码，如果余数为10，则识别码为大写字母XX。例如ISBN号码0-670-82162-4
# 中的识别码4是这样得到的：
# 对067082162这9个数字，从左至右，分别乘以1,2,...,9再求和，即0×1+6×2+……+2×9=158，然后取158mod11的结果4作为识别码。
#
# 你的任务是编写程序判断输入的ISBN号码中识别码是否正确，如果正确，则仅输出Right；如果错误，则输出你认为是正确的ISBN号码。

ibsn = input('输入10位的IBSN码= ')
cd = len(ibsn)
ys = 1
ibsn2 = ibsn[:9]
x = ibsn[9]
n2 = int(x)
sum = 0
if cd == 10:
    for i in ibsn2:
        n = int(i)
        sum = sum + (n * ys)
        ys += 1
    sbm = sum % 11
    if sbm == n2:
        print('正确的ISBN码')
    else:
        print('不正确的ISBN码')

else:
    print('输入的isbn码有误')
