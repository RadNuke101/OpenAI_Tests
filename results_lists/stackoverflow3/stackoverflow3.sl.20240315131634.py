def return_after_4_numbers(input_list):
    output_list = []
    for item in input_list:
        text = item[0]
        index = 0
        count = 0
        for i in range(len(text)):
            if text[i].isdigit():
                count += 1
                if count == 4:
                    index = i + 1
                    break
        output_list.append(text[index:].strip())
    return output_list

input_list = [['geb. 14 oct 1956 Westerkerk HRL'], ['geb. 14 oct 1956 '], ['geb. 15 feb 1987 Westerkerk HRL']]
output = return_after_4_numbers(input_list)
print(output)
