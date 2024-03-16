def remove_dashes(input_list):
    output_list = []
    for sublist in input_list:
        for item in sublist:
            output_list.append(item.replace('-', ''))
    return output_list

input_list = [['801-345-1987'], ['612-554-2000']]
output = remove_dashes(input_list)
print(output)
