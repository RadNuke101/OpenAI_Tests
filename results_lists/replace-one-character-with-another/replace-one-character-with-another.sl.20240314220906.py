def replace_spaces_with_dash(input_list):
    output_list = []
    for item in input_list:
        output_list.append(item[0].replace(" ", "-"))
    return output_list

input_list = [['801 456 8756'], ['978 456 8756']]
print(replace_spaces_with_dash(input_list))
