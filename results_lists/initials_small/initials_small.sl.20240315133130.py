def extract_initials(input_list):
    output = []
    for item in input_list:
        names = item[0].split()
        initials = names[0][0] + '.' + names[1][0] + '.'
        output.append(initials)
    return output

input_list = [['Nancy FreeHafer'], ['Andrew Cencici'], ['Jan Kotas'], ['Mariya Sergienko']]
output = extract_initials(input_list)
print(output)
