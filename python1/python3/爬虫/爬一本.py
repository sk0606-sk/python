import parsel
import requests
mul='http://www.rengongzaowu.com/quinb/14790.html'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'
}
response=requests.get(mul,headers)
response.encoding='utf-8'

selector=parsel.Selector(response.text)
file_name=selector.css('.detail-box .info .top h1::text').get()
href=selector.css('.section-list li a::attr(href)').getall()
for link in href :
    link_jia='http://www.rengongzaowu.com'+link
    response_1=requests.get(link_jia)
    selector_1=parsel.Selector(response_1.text)
    title=selector_1.css('.reader-main .title::text').get()
    content_list=selector_1.css('.reader-main .content p::text').getall()
    content='\n'.join(content_list)
    with open(file_name+'.txt','a',encoding='utf-8')as sk:
        sk.write(title)
        sk.write('\n')
        sk.write(content)
        sk.write('\n')
