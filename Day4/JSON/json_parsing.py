import json

'''
Write json data
'''
data = {}  
data['people'] = []  
data['people'].append({  
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({  
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({  
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

json_file = 'C:\\Projects\\Introduction-To-Python\\Day4\\JSON\\data.json'
with open(json_file, 'w') as outfile:  
    json.dump(data, outfile)

'''
Read json data
'''
with open(json_file) as json_file:  
    data = json.load(json_file)
    #print data
    
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')
    