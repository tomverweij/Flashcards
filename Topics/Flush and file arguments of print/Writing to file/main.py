f_name = "test.txt"
my_string = "A string to be written to a file!"

p_file = open(f_name, 'w')
print(my_string, file=p_file)
p_file.close()