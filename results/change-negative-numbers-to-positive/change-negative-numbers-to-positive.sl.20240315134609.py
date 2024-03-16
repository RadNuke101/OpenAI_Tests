def remove_minus(input_list):
    output_list = []
    for item in input_list:
        if item[0][0] == '-':
            output_list.append(item[0][1:])
        else:
            output_list.append(item[0])
    return output_list

input_list = [['-%134'], ['500'], ['5.125'], ['-%43.00']]
output = remove_minus(input_list)
print(output)
