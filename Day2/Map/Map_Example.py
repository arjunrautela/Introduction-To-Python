#Contains Map built-in function example:

def square_of_num(num):
    return num **2

my_nums = [1,2,3,4,5,6]

print('Output : ', list(map(square_of_num, my_nums)))


# Map With Lambda

print(list(map(lambda x,y : x*y, [1,2,3,4],[1,2,3,4])))


