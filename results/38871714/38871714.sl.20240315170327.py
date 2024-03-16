def remove_brackets(input_list):
    output_list = []
    for sublist in input_list:
        new_sublist = []
        for item in sublist:
            new_item = item.replace('<', '').replace('>', '')
            new_sublist.append(new_item)
        output_list.append(' '.join(new_sublist))
    return output_list

input_list = [['This is a <string>, It should be <changed> to <a> number.'], ['a < 4 and a > 0']]
output = remove_brackets(input_list)
print(output)
