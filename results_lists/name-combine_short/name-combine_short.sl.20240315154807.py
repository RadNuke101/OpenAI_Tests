def combine_names(input_list):
    return [' '.join(name) for name in input_list]

input_list = [['Launa', 'Withers'], ['Lakenya', 'Edison'], ['Brendan', 'Hage'], ['Bradford', 'Lango'], ['Rudolf', 'Akiyama'], ['Lara', 'Constable']]
output = combine_names(input_list)
print(output)
