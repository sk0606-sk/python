import requests
import parsel
url='http://www.rengongzaowu.com/quinb/14790/64216912.html'
requests=requests.get(url)
requests.encoding='utf-8'
selector=parsel.Selector(requests.text)
title=selector.css('.reader-main .title::text').get()
con=selector.css('.reader-main .content p::text').getall()
print(con)
con='\n'.join(con)
f=open('xsw.txt','w',encoding='utf-8')
f.write(title)
f.write('\n')
f.write(con)
f.write('\n')
f.close()