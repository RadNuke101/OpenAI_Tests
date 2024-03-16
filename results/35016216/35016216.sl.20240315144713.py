def find_expression(input_list):
    output = []
    for pair in input_list:
        if 'C0' in pair[0]:
            output.extend(pair)
    return output

input_list = [['C0abc', 'def'], ['aabc', 'def'], ['C0dd', 'qwe'], ['dd', 'qwe']]
print(find_expression(input_list))
