
#移动134、135、136、137、138、139、147、148、150、151、152、157、158、159、165、178、182、183、
#184、187、188、198  13[4-9]
# 14[7,8] 15[012789] 165 178 18[2-4,7-8] 198
#联通130、131、132、140、145、146、155、156、166、185、186、175、176
#13[0-2] 14[0,5,6] 15[5,6] 166 18[5,6] 17[5,6]
#电信133、149、153、180、181、189、177、173、174、191、199
# 133 149 153 18[0-1,9] 17[3-4,7] 19[1,9]
#断输人的手机号码是否合法以及判断其所属的运营商的功能。1 [3-9] [0-9]
#判断是否为手机号
import re
phone=input("请输入一个手机号码")
if re.match(r"[1-3]\d{9}",phone):
    print( re.match(r"[1-3]\d{9}",phone).group())
    #判断运营商
    if re.match(r"13[4-9]|14[7,8]|15[0-2,7-9]|165|178|18[2-4,7-8]|198",phone):
        print("这是一个移动号码")
    elif re.match(r"13[0-2]|14[0,5,6]|15[5,6]|166|18[5,6]|17[5,6]",phone):
        print("这是一个联通号码")
    elif re.match(r"133|149|153|18[0-1,9]|17[3-4,7]|19[1,9]",phone):
        print("这是一个电信号码")
    else:
        print("不合法")
else:
    print("不合法")
