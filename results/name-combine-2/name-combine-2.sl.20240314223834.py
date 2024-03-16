def format_names(input_list):
    output_list = []
    for names in input_list:
        output_list.append(names[0] + ' ' + names[1][0] + '.')
    return output_list

input_list = [['Nancy', 'FreeHafer'], ['Andrew', 'Cencici'], ['Jan', 'Kotas'], ['Mariya', 'Sergienko']]
output = format_names(input_list)
print(output)
