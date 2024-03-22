def return_after_sequence(input_list):
    output = []
    for item in input_list:
        text = item[0]
        index = text.find(' ')
        for _ in range(4):
            index = text.find(' ', index + 1)
        output.append(text[index+1:])
    return output

input_list = [['geb. 14 oct 1956 Westerkerk HRL'], ['geb. 14 oct 1956 '], ['geb. 15 feb 1987 Westerkerk HRL']]
print(return_after_sequence(input_list))
