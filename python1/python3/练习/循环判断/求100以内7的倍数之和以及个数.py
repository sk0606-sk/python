# i=0
# sum=0
# count=0
# while i<100 :
#     i+=1
#     if i%7==0 :
#        sum+=i
#        count += 1
# print(sum,count)
i = 0
sum = 0
count = 0
while i < 100:
    i += 1  # 不要i+=7 因为倒数第二次时 i=98 还是小于100 会再次进行98+7 会多打印一个105
    if i % 7 == 0:
        sum += i
        count += 1
print(sum, count)
