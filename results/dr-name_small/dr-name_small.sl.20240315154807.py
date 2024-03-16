def add_title(input_list):
    return ['Dr. ' + name[0].split()[0] for name in input_list]

input_list = [['Nancy FreeHafer'], ['Andrew Cencici'], ['Jan Kotas'], ['Mariya Sergienko']]
output = add_title(input_list)
print(output)
