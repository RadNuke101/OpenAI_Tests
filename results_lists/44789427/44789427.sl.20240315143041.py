def process_input(input_list):
    result = []
    for item in input_list:
        if item[1] == '1':
            result.append(item[0].split('-')[0])
        elif item[1] == '2':
            result.append(item[0].split('-')[1])
    return result

input_list = [['1/17/16-1/18/17', '1'], ['1/17/16-1/18/17', '2'], ['01/17/2016-01/18/2017', '1'], ['01/17/2016-01/18/2017', '2']]
output = process_input(input_list)
print(output)
