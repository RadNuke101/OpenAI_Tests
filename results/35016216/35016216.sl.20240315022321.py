def return_expression_or_second(input_list):
    output = []
    for item in input_list:
        if 'C0' in item[0]:
            output.extend(item)
    return output

input_list = [['C0abc', 'def'], ['aabc', 'def'], ['C0dd', 'qwe'], ['dd', 'qwe']]
print(return_expression_or_second(input_list))
