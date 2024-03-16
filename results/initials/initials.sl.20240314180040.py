def format_names(input_list):
    output_list = []
    for item in input_list:
        names = item[0].split()
        formatted_name = names[0][0] + '.' + names[1][0] + '.'
        output_list.append(formatted_name)
    return output_list

input_list = [['Nancy FreeHafer'], ['Andrew Cencici'], ['Jan Kotas'], ['Mariya Sergienko']]
output = format_names(input_list)
print(output)
