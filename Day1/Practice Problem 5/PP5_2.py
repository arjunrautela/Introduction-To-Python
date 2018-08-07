#Write a function takes a two-word string and returns True if both words begin with same letter
#animal_crackers('Levelheaded Llama') --> True
#animal_crackers('Crazy Kangaroo') --> False

def animal_crackers(two_word_str):
    return two_word_str.split(' ')[0][0] == two_word_str.split(' ')[1][0]
    '''
        return True
    else:
        return False 
    '''
print('Output : ', animal_crackers('Levelheaded Llama'))

print('Output : ', animal_crackers('Crazy Kangaroos'))