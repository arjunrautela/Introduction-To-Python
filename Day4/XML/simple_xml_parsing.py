import xml.etree.ElementTree as ET

xml_input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''



stuff = ET.fromstring(xml_input)
lst = stuff.findall('users/user')

print('list : ', lst)

print( 'User count: ', len(lst))

for item in lst:
    print( 'Name', item.find('name').text)
    print( 'id', item.find('id').text)
    print ('Attribute', item.get('x'))
    

