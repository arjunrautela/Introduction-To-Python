#Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
#Lesser_of_two_evens(2,4) --> 2
#Lesser_of_two_evens(2,5) --> 5


def lesser_of_two_evens(x,y):
    
    if x %2 ==0 and y%2 == 0:
        return x if x<y else y
        #return lesser

    else:
        #return greater
        return x if x> y else y

print(lesser_of_two_evens(2,3))