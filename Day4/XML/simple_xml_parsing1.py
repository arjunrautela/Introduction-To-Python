import xml.etree.ElementTree as ET

xml_input = '''<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
	<book category="cooking">
		<title lang="en">Everyday Italian</title>
		<author>Giada De Laurentiis</author>
		<year>2005</year>
		<price>30.00</price>
	</book>
	<book category="children">
		<title lang="en">Harry Potter</title>
		<author>J K. Rowling</author>
		<year>2005</year>
		<price>29.99</price>
	</book>
	<book category="web">
		<title lang="en">XQuery Kick Start</title>
		<author>James McGovern</author>
		<author>Per Bothner</author>
		<author>Kurt Cagle</author>
		<author>James Linn</author>
		<author>Vaidyanathan Nagarajan</author>
		<year>2003</year>
		<price>49.99</price>
	</book>
	<book category="web">
		<title lang="en">Learning XML</title>
		<author>Erik T. Ray</author>
		<year>2003</year>
		<price>39.95</price>
	</book>
</bookstore>'''

stuff = ET.fromstring(xml_input)
xml_file_name = 'C:\\Projects\\Introduction-To-Python\\Day4\\XML\\simple.xml'
#stuff = ET.parse(xml_file_name)
#print('root: ', stuff.getroot())
#lst = stuff.findall('.')
#lst = stuff.findall('./book/year')
lst = stuff.findall('book')

print('list : ', lst)
'''
lst = stuff.findall('book')
#lst = stuff.findall('books/book')

print('list : ', lst)

print( 'User count: ', len(lst))

for item in lst:
    print( 'Title : ', item.find('title').text)
    print('Author : ', item.find('author').text)
    print('Title Attribute : ', item.get('category'))
'''