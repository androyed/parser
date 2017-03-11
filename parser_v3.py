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

    main_active.replace("\\\\xa0", "")
    main_active.replace("\\xa0", "" ).replace("['", "").replace("']", "")
    other_active.replace("\\\\xa0", "")
    other_active.replace("\\xa0", "" ).replace("['", "").replace("']", "")

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


def getAllProducts (url):
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        html_code = response.read().decode('utf-8')
        tree = etree.HTML(html_code)
        nodes = tree.xpath('.//div[@class="links"]')
        i = 0

        count_divs_a = tree.xpath('count(.//div[@class="links"]/a/text())')

        while i < count_divs_a  :
    
            a_text = tree.xpath('.//div[@class="links"]/a/text()')[i]

            if a_text == ">":
                prev_page = tree.xpath('.//div[@class="links"]/a/text()')[i-1]
                #there is max_pages 
                max_pages = int(prev_page)
                print ('max_pages=' ,max_pages)
            i = i+1

        cut_url = url[:-1]

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
                print (new_tree.xpath('.//a[@class="clickbleLink"]')[m].get('href'))
                productsXML.appendChild(getProductAttribs((new_tree.xpath('.//a[@class="clickbleLink"]')[m].get('href'))))
                m = m +1
                count_all_pages = count_all_pages + 1
            k = k + 1
        print (count_all_pages)



max_pages = 0


#Cоздаем корневой элемент главной XML-ины
#doc = minidom.Document()

#products
#productsXML = doc.createElement('products')
#doc.appendChild(productsXML)

url = 'http://biosfera.kz/product/category?path=13_451&page=1'
url = 'http://biosfera.kz/product/category?path=13'
#getAllProducts(url)

request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
html_code = response.read().decode('utf-8')
main_tree = etree.HTML(html_code)

n=0

count_categories = main_tree.xpath('count(.//div[@class="sectionsList"]/a)')

while n < (count_categories ) :
    if n != count_categories - 1:
        prev_page = main_tree.xpath('.//div[@class="sectionsList"]/a')[n].get('href')
        prev_page = prev_page + '&page=1'
        print(prev_page)
        n = n + 1
    else:
        prev_page = main_tree.xpath('.//div[@class="sectionsList"]/a')[n].get('href')
        prev_page = prev_page + '?page=1'
        print(prev_page)
        n = n + 1
    
#prev_page = main_tree.xpath('.//div[@class="sectionsList"]/a/text()')

#xml_str = doc.toprettyxml(indent="  ")
#with open("minidom_example.xml", "w") as f:
#    f.write(xml_str)




    


