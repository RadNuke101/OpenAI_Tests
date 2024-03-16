def format_names(input_list):
    output_list = []
    for names in input_list:
        first_letters = [name.split()[0][0] for name in names]
        formatted_name = '.'.join(first_letters) + '.'
        output_list.append(formatted_name)
    return output_list

input_list = [['Nancy FreeHafer'], ['Andrew Cencici'], ['Jan Kotas'], ['Mariya Sergienko']]
output = format_names(input_list)
print(output)
