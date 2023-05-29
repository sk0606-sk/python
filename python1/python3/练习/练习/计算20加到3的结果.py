#第一个递归函数 基线条件是参数等于3
def ji(a):
    if a==3:
        return 3
    return a*ji(a-1)
print(ji(20))