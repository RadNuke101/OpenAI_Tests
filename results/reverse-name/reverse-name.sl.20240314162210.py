def rearrange_names(names):
    return [f'{name[1]} {name[0]}' for name in names]

input_names = [['Launa', 'Withers'], ['Lakenya', 'Edison'], ['Brendan', 'Hage'], ['Bradford', 'Lango'], ['Rudolf', 'Akiyama'], ['Lara', 'Constable']]
output_names = rearrange_names(input_names)
print(output_names)
