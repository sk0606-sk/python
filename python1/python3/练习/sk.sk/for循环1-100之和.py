# sum = 0
# for i in range(1, 101):
#     sum += i
# print(sum)
# def dy(x):
#     if x<=10:
#         print(x)
#     dy(x+1)
# print(dy(1))

def hh(a):
    s=a
    sum = 0
for i in range(1, a):
    sum += i
def h(a):
    if a==1:
        return 1
    return a+h(a-1)
hh(10)




