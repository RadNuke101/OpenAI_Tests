def rearrange_names(input_list):
    return [f'{item[1]} {item[0]}' for item in input_list]

input_list = [['Launa', 'Withers'], ['Lakenya', 'Edison'], ['Brendan', 'Hage'], ['Bradford', 'Lango'], ['Rudolf', 'Akiyama'], ['Lara', 'Constable']]
output = rearrange_names(input_list)
print(output)
