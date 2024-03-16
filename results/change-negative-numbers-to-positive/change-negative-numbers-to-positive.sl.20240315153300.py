def remove_minus(input_list):
    output_list = [item[0].lstrip('-') if item[0].startswith('-') else item[0] for item in input_list]
    return output_list

input_list = [['-%134'], ['500'], ['5.125'], ['-%43.00']]
output = remove_minus(input_list)
print(output)
