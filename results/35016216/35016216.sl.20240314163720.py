def return_expression_or_second(input_list):
    output_list = []
    for item in input_list:
        if 'C0' in item[0]:
            output_list.extend(item)
    return output_list

input_list = [['C0abc', 'def'], ['aabc', 'def'], ['C0dd', 'qwe'], ['dd', 'qwe']]
output = return_expression_or_second(input_list)
print(output)
