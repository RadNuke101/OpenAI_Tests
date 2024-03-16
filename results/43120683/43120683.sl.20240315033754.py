def process_input(input_list):
    output_list = []
    for item in input_list:
        word, num = item[0].split(', ')
        if '1' in num:
            output_list.append(word + ' apple')
        elif '2' in num:
            output_list.append(word + ' bananas')
        elif '3' in num:
            output_list.append(word + ' strawberries')
        elif '4' in num:
            output_list.append(word + ' oranges')
    return output_list

input_list = [['one, 1'], ['two, 2'], ['three, 3'], ['four, 4']]
output = process_input(input_list)
print(output)
