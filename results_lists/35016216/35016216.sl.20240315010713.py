def find_expression(input_list):
    output = []
    for item in input_list:
        if 'C0' in item[0]:
            output.extend(item)
    return output

input_list = [['C0abc', 'def'], ['aabc', 'def'], ['C0dd', 'qwe'], ['dd', 'qwe']]
output = find_expression(input_list)
print(output)
