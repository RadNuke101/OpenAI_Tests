def add_title(names):
    return ['Dr. ' + name[0].split()[0] for name in names]

input_data = [['Nancy FreeHafer'], ['Andrew Cencici'], ['Jan Kotas'], ['Mariya Sergienko']]
output_result = add_title(input_data)
print(output_result)
