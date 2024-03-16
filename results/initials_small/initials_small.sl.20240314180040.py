def format_names(input_list):
    output_list = []
    for names in input_list:
        first_letters = [name.split()[0][0] for name in names]
        output_list.append('.'.join(first_letters) + '.')
    return output_list

input_list = [['Nancy FreeHafer'], ['Andrew Cencici'], ['Jan Kotas'], ['Mariya Sergienko']]
print(format_names(input_list))
