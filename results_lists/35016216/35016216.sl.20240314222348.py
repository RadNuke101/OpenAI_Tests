def process_input(input_list):
    output = []
    for item in input_list:
        if 'C0' in item[0]:
            output.append(item[0])
            output.append(item[1])
        else:
            output.append(item[1])
    return output

input_list = [['C0abc', 'def'], ['aabc', 'def'], ['C0dd', 'qwe'], ['dd', 'qwe']]
print(process_input(input_list))
