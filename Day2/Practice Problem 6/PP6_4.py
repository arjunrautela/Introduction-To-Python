# Using Map calculate square of a number for a given list

def num_square(num):
    return num**2

nums = [1,2,3,4,5,6,7]

print('Square : ' , list(map(num_square, nums)))