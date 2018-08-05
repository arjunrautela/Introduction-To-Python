#Given a string, return a string where for every character in the original there are three characters
#paper_doll('Hello') --> 'HHHeeellllllooo'
#paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii‘


def paper_doll(data):
    result = ''
    for ch in data:
        result += ch * 3
    return result


print('Output :', paper_doll('Hello'))

print('Output :', paper_doll('Mississippi'))