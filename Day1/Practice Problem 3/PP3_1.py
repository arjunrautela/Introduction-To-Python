# Print number * 2 from a given list using for loop

num_list = [1,2,3,4,5,6]
new_list = []
for n in num_list:
    print('Twice of number {} is {}'.format(n, n*2) )
    new_list.append(n*2)

print("New List : ", new_list)