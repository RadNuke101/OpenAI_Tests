def format_names(names):
    return ['{}. {}'.format(name[0][0], name[1]) for name in names]

input_data = [['Launa', 'Withers'], ['Lakenya', 'Edison'], ['Brendan', 'Hage'], ['Bradford', 'Lango'], ['Rudolf', 'Akiyama'], ['Lara', 'Constable']]
output_result = format_names(input_data)
print(output_result)
