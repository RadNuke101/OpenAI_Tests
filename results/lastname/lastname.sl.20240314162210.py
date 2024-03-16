def get_second_word(input_list):
    return [phrase[0].split()[1] for phrase in input_list]

# Test the function with the given input
input_list = [['Nancy FreeHafer'], ['Andrew Cencici'], ['Jan Kotas'], ['Mariya Sergienko']]
output = get_second_word(input_list)
print(output)
