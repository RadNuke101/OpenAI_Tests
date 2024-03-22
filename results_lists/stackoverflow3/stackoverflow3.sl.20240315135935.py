def return_after_sequence(input_list):
    output_list = []
    for item in input_list:
        text = item[0]
        index = text.find('1956') + 4
        output_list.append(text[index:].strip())
    return output_list

input_list = [['geb. 14 oct 1956 Westerkerk HRL'], ['geb. 14 oct 1956 '], ['geb. 15 feb 1987 Westerkerk HRL']]
print(return_after_sequence(input_list))
