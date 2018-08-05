# Using map check string length is even or not

def check_len(str_data):
    if len(str_data) %2 == 0:
        return 'Even'
    else:
        return 'Odd'

words = ['Arjun', 'Sam', 'Nakula']

print(list(map(check_len, words)))