import random
wenjian='ips.txt'
with open(wenjian,'a') as sk:
    for i in range(500):
        suijishu = random.randint(1,254)
        suijishu1=random.randint(64,127)
        xie=sk.writelines(f"192.168.{suijishu1}.{suijishu}\n",)
with open(wenjian,'r')as skk:
    lieb=skk.readlines()
    for i in lieb :
        for x in lieb:
            print(x.count(i))

