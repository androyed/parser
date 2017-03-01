import urllib.request
from lxml import etree

max_pages = 0

url = 'http://biosfera.kz/product/category?path=13_451&page=1'
#url = 'http://biosfera.kz/product/category?path=14_100&page=1'
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
#print (response.read().decode('utf-8'))
html_code = response.read().decode('utf-8')

#tree = etree.parse (html_code)
tree = etree.HTML(html_code)


#nodes = tree.xpath('.//div[@class="links"]/a')
#nodes = tree.xpath('/html/body/div')

nodes = tree.xpath('.//div[@class="links"]')


#for node in nodes:
#    print (node.tag, node.keys(), node.values())
#    #print ('class=', node.get('class')
#    print ('text =', node.text)

i = 0

count_divs_a = tree.xpath('count(.//div[@class="links"]/a/text())')

while i < count_divs_a  :
    
    a_text = tree.xpath('.//div[@class="links"]/a/text()')[i]
    #print ('test ',i,'=', a_text)
    if a_text == ">":
        prev_page = tree.xpath('.//div[@class="links"]/a/text()')[i-1]
        #there is max_pages 
        max_pages = int(prev_page)
        print ('max_pages=' ,max_pages)
    i = i+1



#j = 0
#while j < tree.xpath('count(.//div[@class="lotImage"]/a)'):
#    #print (tree.xpath('.//div[@class="lotImage"]/a')[j].get('href'))
#    print (tree.xpath('.//a[@class="clickbleLink"]')[j].get('href'))
#    j = j +1

cut_url = url[:-1]
#print (cut_url)


#Теперь относительно всех страниц
count_all_pages = 0
k = 1
while k < max_pages+1:
    new_url = cut_url + str(k)
    print ('new_url=', new_url)
    new_request = urllib.request.Request(new_url)
    new_response = urllib.request.urlopen(new_request)
    new_html_code = new_response.read().decode('utf-8')
    new_tree = etree.HTML(new_html_code)
    print ('page=', k)
    m = 0
    while m < new_tree.xpath('count(.//div[@class="lotImage"]/a)'):
        #print (tree.xpath('.//div[@class="lotImage"]/a')[m].get('href'))
        print (new_tree.xpath('.//a[@class="clickbleLink"]')[m].get('href'))
        m = m +1
        count_all_pages = count_all_pages + 1
    k = k + 1
print (count_all_pages)    

#count nodes for parse max_page
#print ('test=', tree.xpath('count(.//div[@class="links"]/a/text())')) 

#http://biosfera.kz/product/category?path=13_451&page=1
#<div class="links">
#<a href="http://biosfera.kz/product/category?path=13_451&amp;page=20">20</a>

#products
#<a class="clickbleLink" href="http://biosfera.kz/product/product?path=13_451&amp;product_id=22335" title="Есть в наличии"></a>

#name_of_product
#<div class="likeH1Tite">Доктор МОМ 20 г мазь в бан. </div>
#or
#<span itemprop="name">Доктор МОМ 20 г мазь в бан.</span>

