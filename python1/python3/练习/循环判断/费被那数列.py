# def fei(shuzi):
#     if shuzi==1 or shuzi==2 :
#         return 1
#     else :
#         return  fei(shuzi-1)+fei(shuzi-2)
# a=[]
# shu=int(input('shu'))
# for i in range(0,shu+1):
#     a.append(fei(shu))
# fei(shu)
# print(a)
#



def he(shu):
    if shu == 1:
        return 1
    else:
        return shu+he(shu-1)
print(he(100))