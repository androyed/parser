import urllib.request
from lxml import etree

from xml.dom import minidom

def getProductAttribs(url):
    new_request = urllib.request.Request(url)
    new_response = urllib.request.urlopen(new_request)
    new_html_code = new_response.read().decode('utf-8')
    new_tree = etree.HTML(new_html_code)

    name = (new_tree.xpath('.//span[@itemprop="name"]/text()')).__str__()
    price = new_tree.xpath('.//div[@id="fix_price"]/text()').__str__()
    main_active = (new_tree.xpath('//*[starts-with(text(),"активн")]/..//text()')).__str__()
    other_active = (new_tree.xpath('//*[preceding::i[starts-with(.,"активн")]][following::i[starts-with(.,"вспомог")]]/text()')).__str__()

    #Создаем элемент XML файла product
    doc = minidom.Document()
    #product
    productXML = doc.createElement('product')

    #url
    urlXML = doc.createElement('url')
    url_text = doc.createTextNode(url)
    urlXML.appendChild(url_text)

    productXML.appendChild(urlXML)

    #name
    nameXML = doc.createElement('name')
    name_text = doc.createTextNode(name)
    nameXML.appendChild(name_text)

    productXML.appendChild(nameXML)
    
    #price
    priceXML = doc.createElement('price')
    price_text = doc.createTextNode(price)
    priceXML.appendChild(price_text)

    productXML.appendChild(priceXML)

    #active
    activeXML = doc.createElement('active')
    active_text = doc.createTextNode(main_active + ',' + other_active)
    activeXML.appendChild(active_text)

    productXML.appendChild(activeXML)

    return productXML


doc = minidom.Document()

#products
productsXML = doc.createElement('products')
doc.appendChild(productsXML)

productsXML.appendChild(getProductAttribs("http://biosfera.kz/product/product?product_id=1446"))



xml_str = doc.toprettyxml(indent="  ")
with open("minidom_example.xml", "w") as f:
    f.write(xml_str)







tree = etree.parse("minidom_example.xml")

mask = "Имудон"
#Работает вытаскивает только имена массивом
nodes = tree.xpath('/products/product/name[contains(., '+ mask +')]/text()')
#Вытаскивает цену массивом
nodes1 = tree.xpath('/products/product/name[contains(., '+ mask +')]//..//price/text()')


print (nodes)
print (nodes1)


"""


new_url = 'http://biosfera.kz/product/product?product_id=1446'
#new_url = 'http://biosfera.kz/product/product?path=13_451&product_id=5623'
#new_url = 'http://biosfera.kz/product/product?path=13_451&product_id=24005'
#new_url = 'http://biosfera.kz/product/product?path=13_451&product_id=13612'
new_request = urllib.request.Request(new_url)
new_response = urllib.request.urlopen(new_request)
new_html_code = new_response.read().decode('utf-8')
new_tree = etree.HTML(new_html_code)

#name
# (new_tree.xpath('.//span[@itemprop="name"]/text()'))
#price
#print(new_tree.xpath('.//div[@id="fix_price"]/text()'))



#print (new_tree.xpath('.//div[@class="lotDiscrTextInc"]/b/text()'))

#active_thug
##print (new_tree.xpath('.//div[@class="lotDiscrTextInc"]/p/text()'))

#print (new_tree.xpath('//*[text()="активные вещества:"]/../text()'))
#the best first 
#print (new_tree.xpath('//*[text()="активные вещества"]/..//text()'))
#Остаток
#print (new_tree.xpath('//*[preceding::i[.="активные вещества"]][following::i[.="вспомогательные вещества"]]/text()'))
#print ('ok')

url_http = new_url 

name = (new_tree.xpath('.//span[@itemprop="name"]/text()')).__str__()
print ('name:' ,name.replace("['", "").replace("']", "") )

price = new_tree.xpath('.//div[@id="fix_price"]/text()').__str__()
print('price:' , price.replace("['", "").replace("']", ""))

main_active = (new_tree.xpath('//*[starts-with(text(),"активн")]/..//text()')).__str__()
print ('акт:',main_active.replace("\\xa0", "" ).replace("['", "").replace("']", ""))

other_active = (new_tree.xpath('//*[preceding::i[starts-with(.,"активн")]][following::i[starts-with(.,"вспомог")]]/text()')).__str__()
print ('Other:',other_active.replace("\\xa0", "" ).replace("['", "").replace("']", ""))


print ('ok')

#http://sergo.eu/blog/online/python-3-sozdanie-xml

#Формируем XML
"""
"""
doc = minidom.Document()

root = doc.createElement('root')
doc.appendChild(root)
 
leaf = doc.createElement('leaf')
text = doc.createTextNode('Text element with attributes')
leaf.appendChild(text)
leaf.setAttribute('color', 'white')
root.appendChild(leaf)
 
leaf_cdata = doc.createElement('leaf_cdata')
cdata = doc.createCDATASection('<em>CData</em> can contain <strong>HTML tags</strong> without encoding')
leaf_cdata.appendChild(cdata)
root.appendChild(leaf_cdata)
 
branch = doc.createElement('branch')
branch.appendChild(leaf.cloneNode(True))
root.appendChild(branch)
 
mixed = doc.createElement('mixed')
mixed_leaf = leaf.cloneNode(True)
mixed_leaf.setAttribute('color', 'black')
mixed_leaf.setAttribute('state', 'modified')
mixed.appendChild(mixed_leaf)
mixed_text = doc.createTextNode('Do not use mixed elements if it possible.')
mixed.appendChild(mixed_text)
root.appendChild(mixed)
 
xml_str = doc.toprettyxml(indent="  ")
with open("minidom_example.xml", "w") as f:
    f.write(xml_str)
"""

"""
<?xml version="1.0" ?>
<root>
  <leaf color="white">Text element with attributes</leaf>
  <leaf_cdata>
<![CDATA[<em>CData</em> can contain <strong>HTML tags</strong> without encoding]]>  </leaf_cdata>
  <branch>
    <leaf color="white">Text element with attributes</leaf>
  </branch>
  <mixed>
    <leaf color="black" state="modified">Text element with attributes</leaf>
    Do not use mixed elements if it possible.
  </mixed>
</root>
"""
"""
<products>
    <product>
        <url> </url>    
        <name> </name>
        <price> </price>
        <active> </active>
    </product>
</products>
"""

#то что надо
"""

doc = minidom.Document()

#products
productsXML = doc.createElement('products')
doc.appendChild(productsXML)

#product

productXML = doc.createElement('product')

#url

urlXML = doc.createElement('url')
url_text = doc.createTextNode(url_http)
urlXML.appendChild(url_text)

productXML.appendChild(urlXML)

#name

nameXML = doc.createElement('name')
name_text = doc.createTextNode(name)
nameXML.appendChild(name_text)

productXML.appendChild(nameXML)

#price

priceXML = doc.createElement('price')
price_text = doc.createTextNode(price)
priceXML.appendChild(price_text)

productXML.appendChild(priceXML)

#active

activeXML = doc.createElement('active')
active_text = doc.createTextNode(main_active + ',' + other_active)
activeXML.appendChild(active_text)

productXML.appendChild(activeXML)


productsXML.appendChild(productXML)


xml_str = doc.toprettyxml(indent="  ")
with open("minidom_example.xml", "w") as f:
    f.write(xml_str)
"""
"""
tree = etree.parse("minidom_example.xml")

mask = "Имудон"
#Работает вытаскивает только имена массивом
nodes = tree.xpath('/products/product/name[contains(., '+ mask +')]/text()')
#Вытаскивает цену массивом
nodes1 = tree.xpath('/products/product/name[contains(., '+ mask +')]//..//price/text()')


print (nodes)
print (nodes1)


<products>
    <product>
        <url> </url>    
        <name> </name>
        <price> </price>
        <active> </active>
    </product>
</products>

doc = minidom.Document()

#root
productsXML = doc.createElement('products')
doc.appendChild(products)

#product

productXML = doc.createElement('product')

#url

urlXML = doc.cteateElement('url')
url_text = doc.createTextNode(url_http)
urlXML.appendChild(url_text)

productXML.appendChild(urlXML)

#name

nameXML = doc.createElement('name')
name_text = doc.createTextNode(name)
nameXML.appendChild(name_next)

productXML.appendChild(nameXML)

#price

priceXML = doc.createElement('price')
price_text = doc.createTextNode(price)
priceXML.appendChild(price_next)

productXML.appendChild(priceXML)

#active




products.appendChild(product)

"""

