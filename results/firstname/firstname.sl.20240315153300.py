def return_first_word(input_list):
    output_list = [name[0].split()[0] for name in input_list]
    return output_list

input_list = [['Nancy FreeHafer'], ['Andrew Cencici'], ['Jan Kotas'], ['Mariya Sergienko']]
print(return_first_word(input_list))
