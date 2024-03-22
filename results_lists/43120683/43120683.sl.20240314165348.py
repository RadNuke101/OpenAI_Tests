def process_input(input_list):
    output_list = []
    for item in input_list:
        word = item[0].split(',')[0]
        number = int(item[0].split(',')[1])
        if number == 1:
            output_list.append(word + ' apple')
        elif number == 2:
            output_list.append(word + ' bananas')
        elif number == 3:
            output_list.append(word + ' strawberries')
        elif number == 4:
            output_list.append(word + ' oranges')
    return output_list

input_list = [['one, 1'], ['two, 2'], ['three, 3'], ['four, 4']]
output = process_input(input_list)
print(output)
