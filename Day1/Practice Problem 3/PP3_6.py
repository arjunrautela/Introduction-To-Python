#Print items of a dictionary

d = {"Fname": "Arjun", "Lname":"Rautela", "Dept":"B&P", "Team":"CTAM"}

for key in d:
    print("Key :", key)
    print("Value : ", d[key])


print ("All the keys in d : ", list(d.keys()))
print("All the values in d : ", list(d.values()))

#key value in a form of tuple

print("Key value pair in a form of tuple : ", list(d.items()))


for k,v in d.items():
    print ('key : ', k, 'and value :',v)