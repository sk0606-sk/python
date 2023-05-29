def hui_wen(s):
    if len(s)<2:        #递归和循环很类似 循环判断条件满足就执行循环体 不满足则结束循环 对应递归就是 不能再细分下去的条件就是线性条件
        return True     #可以分下去的条间就是递归条件
    elif s[0]!=s[-1]:    #这部分就是细分条件的规则
        return False
    else:
        return hui_wen(s[1:-1])    # 递归条件
print(hui_wen('12321'))
