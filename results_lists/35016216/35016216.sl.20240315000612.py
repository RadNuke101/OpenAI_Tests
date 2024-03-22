def process_input(input_list):
    output_list = []
    for pair in input_list:
        if 'C0' in pair[0]:
            output_list.extend(pair)
    return output_list

input_list = [['C0abc', 'def'], ['aabc', 'def'], ['C0dd', 'qwe'], ['dd', 'qwe']]
output = process_input(input_list)
print(output)
