def second_word(input_list):
    return [phrase[0].split()[1] for phrase in input_list]

input_list = [['Nancy FreeHafer'], ['Andrew Cencici'], ['Jan Kotas'], ['Mariya Sergienko']]
output = second_word(input_list)
print(output)
