def get_first_word(input_list):
    return [name[0].split()[0] for name in input_list]

# Test the function
input_list = [['Nancy FreeHafer'], ['Andrew Cencici'], ['Jan Kotas'], ['Mariya Sergienko']]
print(get_first_word(input_list))
