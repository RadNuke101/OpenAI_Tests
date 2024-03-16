def rearrange_names(input_list):
    return [f"{name[1]} {name[0]}" for name in input_list]

input_list = [['Launa', 'Withers'], ['Lakenya', 'Edison'], ['Brendan', 'Hage'], ['Bradford', 'Lango'], ['Rudolf', 'Akiyama'], ['Lara', 'Constable']]
output_list = rearrange_names(input_list)
print(output_list)
