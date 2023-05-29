import re
# one='this，sksks213213'
# two='23.adadaad'
# k=re.match(r'\d',one)
# s=re.match(r'\d',two)
# print(s.group(0))
# k=re.search(r'\d',one)
# s=re.search(r'\d',two)
# print(k.group())
# print(s.group())
# k=re.findall(r'\d',one)
# s=re.findall(r'\d',two)
# print(s)
# print(k)
print('输入电话号码')
hm=input()
cd=len(hm)
if cd==11:#可以用$
    if re.match(r'1[3-9]\d{9}',hm):
        print('合法')
        if re.match(r"13[4-9]|14[7,8]|15[0-2,7-9]|165|178|18[2-4,7-8]|198",hm):
            print("这是一个移动号码")
        elif re.match(r"13[0-2]|14[0,5,6]|15[5,6]|166|18[5,6]|17[5,6]",hm):
            print("这是一个联通号码")
        elif re.match(r"133|149|153|18[0-1,9]|17[3-4,7]|19[1,9]",hm):
            print("这是一个电信号码")

else:
    print('不合法')