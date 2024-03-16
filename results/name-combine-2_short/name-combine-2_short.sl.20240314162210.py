def format_names(inputs):
    return [f"{input[0]} {input[1][0]}." for input in inputs]

# Test the function with the given input
inputs = [['Nancy', 'FreeHafer'], ['Andrew', 'Cencici'], ['Jan', 'Kotas'], ['Mariya', 'Sergienko']]
output = format_names(inputs)
print(output)
