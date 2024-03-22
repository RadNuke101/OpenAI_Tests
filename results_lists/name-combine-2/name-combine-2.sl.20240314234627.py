def format_names(inputs):
    output = []
    for input_pair in inputs:
        output.append(input_pair[0] + ' ' + input_pair[1][0] + '.')
    return output

inputs = [['Nancy', 'FreeHafer'], ['Andrew', 'Cencici'], ['Jan', 'Kotas'], ['Mariya', 'Sergienko']]
print(format_names(inputs))
