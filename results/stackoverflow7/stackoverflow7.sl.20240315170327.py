def remove_second_input(input_list):
    output_list = []
    for item in input_list:
        output_item = item[0].split(' ')[0]
        if len(item) > 1:
            output_item += ' ' + item[1]
        output_list.append(output_item)
    return output_list

input_list = [['Item 1 AQ-S810W-2AVDF', 'AQ-S810W-2AVDF'], ['Item 2 AQ-230A-1DUQ', 'AQ-230A']]
output = remove_second_input(input_list)
print(output)
