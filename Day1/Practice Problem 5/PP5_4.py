#Given a sentence, return a sentence with the words reversed
#master_yoda('I am home') --> 'home am I'
#master_yoda('We are ready') --> 'ready are We'

def master_yoda(sentence):
    split_sent = sentence.split(' ')
    return split_sent[::-1]

print('Output : ', master_yoda('I am home'))


print('Output : ', master_yoda('We are ready'))
