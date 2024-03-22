def remove_brackets(input_list):
    output_list = []
    for item in input_list:
        new_item = item[0].replace('<', '').replace('>', '')
        output_list.append(new_item)
    return output_list

input_list = [['This is a <string>, It should be <changed> to <a> number.'], ['a < 4 and a > 0']]
output = remove_brackets(input_list)
print(output)
