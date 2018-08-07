import re

def starts_with():
    hand = open('mbox.txt')
    for line in hand:
        line = line.rstrip()
        if re.search('^From:', line):
            print line
    hand.close()    


def char_match():
    hand = open('mbox.txt')
    for line in hand:
        line = line.rstrip()
        if re.search('^F...m', line):
            print line
    hand.close()

def one_or_more():
    hand = open('mbox.txt')
    for line in hand:
        line = line.strip()
        if re.search('^From:.+n@', line):
            print line
    hand.close()
def extract_data():
    s = 'Hello from csev@umich.edu to cwen@iupui.edu about the meeting @2PM'
    lst = re.findall('\S+@\S+', s)
    print lst

def extract_data_file():
    hand = open('mbox.txt')
    for line in hand:
        line = line.rstrip()
        #lst = re.findall('\S+@\S+', line)
        lst = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', line)
        print lst
    hand.close()
if __name__ == "__main__":
    #starts_with()
    #char_match()
    #one_or_more()
    #extract_data()
    extract_data_file()