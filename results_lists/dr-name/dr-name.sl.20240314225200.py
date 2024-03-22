def add_title(input_list):
    output_list = ['Dr. ' + name[0].split()[0] for name in input_list]
    return output_list

input_list = [['Nancy FreeHafer'], ['Andrew Cencici'], ['Jan Kotas'], ['Mariya Sergienko']]
print(add_title(input_list))
