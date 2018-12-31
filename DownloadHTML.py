import requests
from lxml import html
import time


#Четыре одинаковых участка кода выгрузки одной страницы с разным таймаутом, в дальнейшем выделю в одну функцию download
#пока не трогаю. Ведь "Работает, не трожь" :)


num = 608200 # надо выделить в отдельный txt, но пока приходится менять вручную после каждого запуска.
for i in range(3000):
    _str = 'T' + str(num) + '/'
    url = 'https://www.devexpress.com/Support/Center/Question/Details/'+ _str
    r = requests.get(url)
    text = r.text.encode('cp1251', errors='replace')
    tree = html.fromstring(text)
    post = tree.xpath('//div[@class = "edited-text"]/text()')
    _str = ''
    for i in post:
        _str += i
        _str += '\n'
    print(_str.__len__())
    if _str.__len__()>100:
        #   write to test-file
        with open('HTML/' + str(num)+'.html', 'wb') as output_file:
            output_file.write(r.text.encode('cp1251', errors='replace'))
        with open('HTML/' + str(num)+'.txt', 'wb') as output_file:
            output_file.write(_str.encode('utf-8'))
    time.sleep(1)
    num+=1
    _str = 'T' + str(num) + '/'
    url = 'https://www.devexpress.com/Support/Center/Question/Details/'+ _str
    r = requests.get(url)
    text = r.text.encode('cp1251', errors='replace')
    tree = html.fromstring(text)
    post = tree.xpath('//div[@class = "edited-text"]/text()')
    _str = ''
    for i in post:
        _str += i
        _str += '\n'
    print(_str.__len__())
    if _str.__len__()>100:
        #   write to test-file
        with open('HTML/' + str(num)+'.html', 'wb') as output_file:
            output_file.write(r.text.encode('cp1251', errors='replace'))
        with open('HTML/' + str(num)+'.txt', 'wb') as output_file:
            output_file.write(_str.encode('utf-8'))
    time.sleep(0.9)
    num+=1

    _str = 'T' + str(num) + '/'
    print(num)
    url = 'https://www.devexpress.com/Support/Center/Question/Details/'+ _str
    r = requests.get(url)
    text = r.text.encode('cp1251', errors='replace')
    tree = html.fromstring(text)
    post = tree.xpath('//div[@class = "edited-text"]/text()')
    _str = ''
    for i in post:
        _str += i
        _str += '\n'
    print(_str.__len__())
    if _str.__len__()>100:
        #   write to test-file
        with open('HTML/' + str(num)+'.html', 'wb') as output_file:
            output_file.write(r.text.encode('cp1251', errors='replace'))
        with open('HTML/' + str(num)+'.txt', 'wb') as output_file:
            output_file.write(_str.encode('utf-8'))
    time.sleep(1.1)
    num+=1
#print(type(text))


