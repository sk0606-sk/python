numbers = [23, 55, 44, 33, 1, 2, 4, 6, 8]  # 列表 索引从0开始
jishu = []  # 定义空的列表
oushu = []
for num in numbers:  # num 临时变量 numbers 要被遍历的对象 遍历的方式 多个对象 会逐一遍历
    # 一个对象会 遍历对象里面的组成
    if num % 2 == 0:
        oushu.append(num)  # append 附加 格式是 变量.append(要被附加的值得变量)
    else:
        jishu.append(num)
print(jishu)
print(oushu)
