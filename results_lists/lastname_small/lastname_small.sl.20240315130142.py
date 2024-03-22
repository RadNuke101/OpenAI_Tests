def get_second_word(input_list):
    return [name[0].split()[1] for name in input_list]

input_list = [['Nancy FreeHafer'], ['Andrew Cencici'], ['Jan Kotas'], ['Mariya Sergienko']]
output = get_second_word(input_list)
print(output)
