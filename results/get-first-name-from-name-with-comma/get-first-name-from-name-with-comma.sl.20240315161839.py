def process_input(data):
    result = []
    for item in data:
        name, num = item[0].split(',')
        if item[1] == '1':
            result.append(name.split(',')[1])
        elif item[1] == '2':
            result.append(name.split(',')[0])
    return result

input_data = [['Chang,Amy', '1'], ['Chang,Amy', '2'], ['smith,bobby', '2'], ['smith,bobby', '1']]
output_data = process_input(input_data)
print(output_data)
