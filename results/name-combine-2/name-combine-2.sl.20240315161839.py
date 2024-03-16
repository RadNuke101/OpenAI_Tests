def format_names(inputs):
    output = []
    for pair in inputs:
        formatted_name = pair[0] + ' ' + pair[1][0] + '.'
        output.append(formatted_name)
    return output

# Test the function with the given input
inputs = [['Nancy', 'FreeHafer'], ['Andrew', 'Cencici'], ['Jan', 'Kotas'], ['Mariya', 'Sergienko']]
print(format_names(inputs))
