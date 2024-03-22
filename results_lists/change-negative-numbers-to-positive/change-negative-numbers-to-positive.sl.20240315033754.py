def remove_dash(input_list):
    output_list = [x[0].lstrip('-') if x[0][0] == '-' else x[0] for x in input_list]
    return output_list

input_list = [['-%134'], ['500'], ['5.125'], ['-%43.00']]
output = remove_dash(input_list)
print(output)
