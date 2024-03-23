def return_after_sequence(input_list):
    output_list = []
    for item in input_list:
        text = item[0]
        index = text.find(' ')
        for i in range(4):
            index = text.find(' ', index + 1)
        output_list.append(text[index+1:])
    return output_list

input_list = [['geb. 14 oct 1956 Westerkerk HRL'], ['geb. 14 oct 1956 '], ['geb. 15 feb 1987 Westerkerk HRL']]
output = return_after_sequence(input_list)
print(output)