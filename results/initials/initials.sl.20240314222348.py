def format_names(input_list):
    output = []
    for names in input_list:
        first_letters = [name.split()[0][0] for name in names]
        output.append('.'.join(first_letters) + '.')
    return output

input_list = [['Nancy FreeHafer'], ['Andrew Cencici'], ['Jan Kotas'], ['Mariya Sergienko']]
output = format_names(input_list)
print(output)
