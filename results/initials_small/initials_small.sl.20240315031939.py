def extract_initials(input_list):
    output_list = []
    for item in input_list:
        words = item[0].split()
        initials = words[0][0] + '.' + words[1][0] + '.'
        output_list.append(initials)
    return output_list

input_list = [['Nancy FreeHafer'], ['Andrew Cencici'], ['Jan Kotas'], ['Mariya Sergienko']]
output = extract_initials(input_list)
print(output)
