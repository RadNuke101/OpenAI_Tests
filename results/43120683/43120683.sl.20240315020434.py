def process_input(input_list):
    output_list = []
    for item in input_list:
        first_word = item[0].split(',')[0]
        num = int(item[1].strip())
        if num == 1:
            output_list.append(first_word + ' apple')
        elif num == 2:
            output_list.append(first_word + ' bananas')
        elif num == 3:
            output_list.append(first_word + ' strawberries')
        elif num == 4:
            output_list.append(first_word + ' oranges')
    
    return output_list

input_list = [['one, 1'], ['two, 2'], ['three, 3'], ['four, 4']]
output = process_input(input_list)
print(output)
