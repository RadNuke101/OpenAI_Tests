def process_input(input_list):
    result = []
    for item in input_list:
        name, num = item[0].split(',')
        if item[1] == '1':
            result.append(name)
        elif item[1] == '2':
            result.append(num)
    return result

input_list = [['Chang,Amy', '1'], ['Chang,Amy', '2'], ['smith,bobby', '2'], ['smith,bobby', '1']]
output = process_input(input_list)
print(output)
