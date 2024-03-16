def process_input(input_list):
    output = []
    for item in input_list:
        name, num = item[0].split(',')
        if item[1] == '1':
            output.append(name.split(',')[1])
        elif item[1] == '2':
            output.append(name.split(',')[0])
    return output

input_list = [['Chang,Amy', '1'], ['Chang,Amy', '2'], ['smith,bobby', '2'], ['smith,bobby', '1']]
output = process_input(input_list)
print(output)
