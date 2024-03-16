def format_names(inputs):
    output = []
    for pair in inputs:
        output.append(pair[0] + ' ' + pair[1][0] + '.')
    return output

inputs = [['Nancy', 'FreeHafer'], ['Andrew', 'Cencici'], ['Jan', 'Kotas'], ['Mariya', 'Sergienko']]
print(format_names(inputs))
