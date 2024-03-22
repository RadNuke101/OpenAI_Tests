def get_first_word(input_list):
    return [name[0].split()[0] for name in input_list]

input_list = [['Nancy FreeHafer'], ['Andrew Cencici'], ['Jan Kotas'], ['Mariya Sergienko']]
output = get_first_word(input_list)
print(output)
