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

#stuff = ET.fromstring(xml_input)
stuff = ET.parse('simple.xml')
print('root: ', stuff.getroot())
lst = stuff.findall('books/book')

print('list : ', lst)

print( 'User count: ', len(lst))

for item in lst:
    print( 'Title : ', item.find('title').text)
    print('Author : ', item.find('author').text)
    print('Title Attribute : ', item.get('category'))
