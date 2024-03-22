def remove_dash(input_list):
    output_list = []
    for sublist in input_list:
        for item in sublist:
            if item.startswith("-"):
                output_list.append(item[1:])
            else:
                output_list.append(item)
    return output_list

input_list = [['-%134'], ['500'], ['5.125'], ['-%43.00']]
output = remove_dash(input_list)
print(output)
