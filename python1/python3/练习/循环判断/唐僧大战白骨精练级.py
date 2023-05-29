# 1、练级

# -提升玩家的攻击力和生命值
xz = int(input('选择1.2.3 '))
if xz == 1:
    i = int(input('几级'))
    while i < i + 10:
        i += 1
        g = i
        s = i
print(f'你的身份是->唐僧<-,你的攻击力是：{g}你的生命值是：{s}')
print()
print('''请选择你要进行的操作
         1.练级
         2.打Boss`
         3.逃跑
         ''')
