a = dict(name='sk', age='18', address='nx')
print(a)
# 双值子序列
print(a.values())
print(a.keys())
print(a.items())
for i, v in a.items():
    print(i, '=', v)

# items它找的是键值对 键值对里面有两个元素 如果遍历只有一个临时变量承接 对那么
# 输出的直接就是键值对 如果有两个变量承接键值对那么 它会是第一个临时变量会承接keys
# 第二个变量会承接 values
