def return_first_word(input_list):
    return [phrase[0].split()[0] for phrase in input_list]

input_list = [['Nancy FreeHafer'], ['Andrew Cencici'], ['Jan Kotas'], ['Mariya Sergienko']]
output = return_first_word(input_list)
print(output)
