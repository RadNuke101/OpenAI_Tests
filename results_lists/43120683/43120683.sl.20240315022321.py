def process_input(input_list):
    output = []
    for item in input_list:
        word, num = item[0].split(', ')
        if '1' in num:
            output.append(word + ' apple')
        elif '2' in num:
            output.append(word + ' bananas')
        elif '3' in num:
            output.append(word + ' strawberries')
        elif '4' in num:
            output.append(word + ' oranges')
    return output

input_list = [['one, 1'], ['two, 2'], ['three, 3'], ['four, 4']]
output = process_input(input_list)
print(output)
