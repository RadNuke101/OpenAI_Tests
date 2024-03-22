def add_title(names):
    return ['Dr. ' + name[0].split()[0] for name in names]

# Test the function with the provided input
input_names = [['Nancy FreeHafer'], ['Andrew Cencici'], ['Jan Kotas'], ['Mariya Sergienko']]
output_names = add_title(input_names)
print(output_names)
