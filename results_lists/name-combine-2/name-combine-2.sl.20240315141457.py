def format_names(inputs):
    output = []
    for names in inputs:
        formatted_name = names[0] + ' ' + names[1][0] + '.'
        output.append(formatted_name)
    return output

# Test the function
inputs = [['Nancy', 'FreeHafer'], ['Andrew', 'Cencici'], ['Jan', 'Kotas'], ['Mariya', 'Sergienko']]
print(format_names(inputs))
