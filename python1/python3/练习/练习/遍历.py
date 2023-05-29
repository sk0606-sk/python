# a = input('输入字符串')
# count = 0
# for i in a:
#     if i == 'a':
#         count += 1
# print(count)
#     1.输入字符串
#     3.遍历
#     4.定义计数器
#      5.
# 用range遍历
zf = input('请输入字符串')
count_zm = 0
count_sz = 0
count_qt = 0
for i in zf:
    if i.isdigit():
        count_sz += 1
    elif i.isalpha():
        count_zm += 1
    else:
        count_qt += 1
print(count_zm, '字母数')
print(count_sz, '数字数')
print(count_qt, '其他')
