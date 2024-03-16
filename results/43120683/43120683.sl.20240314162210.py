def process_input(input_list):
    output_list = []
    for item in input_list:
        word = item[0].split(',')[0]
        num = int(item[0].split(',')[1].strip())
        if num == 1:
            output_list.append(word + ' apple')
        elif num == 2:
            output_list.append(word + ' bananas')
        elif num == 3:
            output_list.append(word + ' strawberries')
        elif num == 4:
            output_list.append(word + ' oranges')
    return output_list

input_list = [['one, 1'], ['two, 2'], ['three, 3'], ['four, 4']]
output = process_input(input_list)
print(output)
