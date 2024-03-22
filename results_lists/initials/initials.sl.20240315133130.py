def first_letters(input_list):
    output = []
    for item in input_list:
        words = item[0].split()
        first_letters = [word[0].upper() for word in words]
        output.append('.'.join(first_letters) + '.')
    return output

input_list = [['Nancy FreeHafer'], ['Andrew Cencici'], ['Jan Kotas'], ['Mariya Sergienko']]
print(first_letters(input_list))
