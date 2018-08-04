'''
Given words = ['asd', 'aaaa', 'uiwe', 'tew', 'tree', 'point', 'art', 'paint'] 
     create the following dictionary (by using looping constructs) :	
    {'a': ['asd', 'aaaa', 'art'], 'p': ['point', 'paint'], 'u': ['uiwe'], 't': ['tew', 'tree']}
'''

words = ['asd', 'aaaa', 'uiwe', 'tew', 'tree', 'point', 'art', 'paint']

word_dict = {}
for word in words:
    if word[0] not in word_dict:
        word_dict[word[0]] = [word]
    else:
        word_dict[word[0]].append(word)

print("Final Dict : ", word_dict)