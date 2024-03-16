def format_names(names):
    formatted_names = []
    for name in names:
        formatted_names.append(name[0][0] + '. ' + name[1])
    return formatted_names

input_names = [['Launa', 'Withers'], ['Lakenya', 'Edison'], ['Brendan', 'Hage'], ['Bradford', 'Lango'], ['Rudolf', 'Akiyama'], ['Lara', 'Constable']]
output_names = format_names(input_names)
print(output_names)
