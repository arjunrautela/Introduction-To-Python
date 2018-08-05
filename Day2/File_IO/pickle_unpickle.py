# Example of pickle and unpickle

import pickle

data = ['name', 'location', 'date', 'position']

file_name = "pickle_data"
obj = open(file_name, 'wb')

pickle.dump(data, obj)

obj.close()

obj_r = open(file_name, 'rb')
r_data = pickle.load(obj_r)
print(r_data)
obj_r.close()