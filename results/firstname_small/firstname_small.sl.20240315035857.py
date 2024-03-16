def get_first_word(input_list):
    output_list = [item[0].split()[0] for item in input_list]
    return output_list

input_list = [['Nancy FreeHafer'], ['Andrew Cencici'], ['Jan Kotas'], ['Mariya Sergienko']]
print(get_first_word(input_list))
