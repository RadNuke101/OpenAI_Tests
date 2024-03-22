def add_title(input_list):
    output_list = []
    for name in input_list:
        output_list.append("Dr. " + name[0].split()[0])
    return output_list

input_list = [['Nancy FreeHafer'], ['Andrew Cencici'], ['Jan Kotas'], ['Mariya Sergienko']]
print(add_title(input_list))
