#Create a list containing only even numbers from a given list
# Example :  ‘[1,2,3,4,5,6]’  [2,4,6]

num_list = [1,2,3,4,5,6]

print([n for n in num_list if n %2 ==0])