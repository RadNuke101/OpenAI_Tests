def remove_symbols(input_list):
    output_list = []
    for sublist in input_list:
        output_sublist = []
        for item in sublist:
            item = item.replace('<', '').replace('>', '')
            output_sublist.append(item)
        output_list.append(' '.join(output_sublist))
    return output_list

input_list = [['This is a <string>, It should be <changed> to <a> number.'], ['a < 4 and a > 0']]
output = remove_symbols(input_list)
print(output)
