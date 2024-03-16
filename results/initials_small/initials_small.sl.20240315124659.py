def get_initials(input_list):
    output = []
    for item in input_list:
        words = item[0].split()
        initials = words[0][0].upper() + '.' + words[1][0].upper() + '.'
        output.append(initials)
    return output

input_list = [['Nancy FreeHafer'], ['Andrew Cencici'], ['Jan Kotas'], ['Mariya Sergienko']]
output = get_initials(input_list)
print(output)
