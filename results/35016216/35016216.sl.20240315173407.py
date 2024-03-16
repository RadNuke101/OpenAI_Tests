def check_expression(input_list):
    output_list = []
    for item in input_list:
        if 'C0' in item[0]:
            output_list.extend(item)
    return output_list

input_list = [['C0abc', 'def'], ['aabc', 'def'], ['C0dd', 'qwe'], ['dd', 'qwe']]
output = check_expression(input_list)
print(output)
