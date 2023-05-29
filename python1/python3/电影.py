import re
read=open('电影.txt','r',encoding='utf-8').read()
title=r'"title":"(.*?)"'
s=re.compile(title)
t=s.findall(read)
print(t)
ra=r'"rating":\["(.*?)","\d+"\]'
r=re.compile(ra)
rr=r.findall(read)
print(rr)
rank=r'"rank":(\d+)'
rankk=re.compile(rank)
rankkk=rankk.findall(read)
print(rankkk)
for i in range(20):
    print(rankkk[i],  t[i], rr[i]       )