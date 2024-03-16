def rearrange_names(names):
    return [f"{name[1]} {name[0]}" for name in names]

input_data = [['Launa', 'Withers'], ['Lakenya', 'Edison'], ['Brendan', 'Hage'], ['Bradford', 'Lango'], ['Rudolf', 'Akiyama'], ['Lara', 'Constable']]
output_result = rearrange_names(input_data)
print(output_result)
