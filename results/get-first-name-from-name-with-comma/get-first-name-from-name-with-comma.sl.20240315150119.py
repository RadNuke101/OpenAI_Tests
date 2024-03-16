def process_input(input_list):
    output_list = []
    for item in input_list:
        name, option = item[0].split(',')
        if item[1] == '1':
            output_list.append(name)
        elif item[1] == '2':
            output_list.append(option)
    return output_list

input_list = [['Chang,Amy', '1'], ['Chang,Amy', '2'], ['smith,bobby', '2'], ['smith,bobby', '1']]
output = process_input(input_list)
print(output)
