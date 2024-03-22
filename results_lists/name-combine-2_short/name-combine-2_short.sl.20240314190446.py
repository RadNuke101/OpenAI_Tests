def format_names(inputs):
    output = []
    for names in inputs:
        output.append(names[0] + ' ' + names[1][0] + '.')
    return output

input_data = [['Nancy', 'FreeHafer'], ['Andrew', 'Cencici'], ['Jan', 'Kotas'], ['Mariya', 'Sergienko']]
print(format_names(input_data))
