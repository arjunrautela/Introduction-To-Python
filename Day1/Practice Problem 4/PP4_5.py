# Nested List comprehension
lst = [ x**2 for x in [x**2 for x in range(11)]]
print("Nested List : ", lst)