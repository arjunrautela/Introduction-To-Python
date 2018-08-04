#Convert F to C of a list of F temperature using List comp

temp_f_list = [40,50,60,70]

temp_c_list = [(temp-32)*5/9 for temp in temp_f_list]

print("List of Temp in Celcius : ", temp_c_list)