
print('请输入要做的四则运算')
print('加法1，减法2，乘法3，除法4')
xz=input()
if xz=='1':
    print('请输入数字')

    def jia_fa(a, b):
        a + b
        return a + b
    print(jia_fa(float(input('第一个数字')),float(input('第二个数字'))))
elif xz=='2':
    def jian_fa(a, b):
        a - b
        return a - b
    print(jian_fa(float(input('第一个数字')),float(input('第二个数字'))))
elif xz=='3':
    def cheng(a, b):
        a * b
        return a * b
    print(cheng(float(input('第一个数字')),float(input('第二个数字'))))
elif xz=='4':
    def chu(a, b):
        a / b
        return a / b
    print(chu(float(input('第一个数字')),float(input('第二个数字'))))
else :
    print('有誤')
