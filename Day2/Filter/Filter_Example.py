# Filter Built-in function example

def check_evens(num):
    return num%2 == 0

nums = [1,2,3,4,5,6,7,8,9]

print(list(filter(check_evens, nums)))