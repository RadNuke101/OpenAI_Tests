def get_second_word(input_list):
    return [x[0].split()[1] for x in input_list]

input_list = [['Nancy FreeHafer'], ['Andrew Cencici'], ['Jan Kotas'], ['Mariya Sergienko']]
output = get_second_word(input_list)
print(output)
