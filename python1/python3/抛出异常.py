print('输入名字')
name=input()
try:
    print('输入年龄')
    age=int(input())
except  Exception as e :
    print(f'错误类型为{e}请重新输入')
try:
    print('输入收入')
    shoru=int(input())
except  Exception as e :
    print(f'错误类型为{e}请重新输入')     
try:
    if len(name)<2 or len(name)>18 or age <18 or age >60 or  shoru <2500:
        raise ValueError('条件不满足')
except Exception as e :
    print(f'捕获错误 {e}')




