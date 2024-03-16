def return_after_4_numbers(input_list):
    output = []
    for item in input_list:
        text = item[0]
        index = 0
        count = 0
        for i, char in enumerate(text):
            if char.isdigit():
                count += 1
                if count == 4:
                    index = i + 1
                    break
        output.append(text[index:])
    return output

input_list = [['geb. 14 oct 1956 Westerkerk HRL'], ['geb. 14 oct 1956 '], ['geb. 15 feb 1987 Westerkerk HRL']]
print(return_after_4_numbers(input_list))
