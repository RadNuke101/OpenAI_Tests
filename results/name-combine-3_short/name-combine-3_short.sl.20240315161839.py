def format_names(names):
    formatted_names = []
    for name in names:
        formatted_names.append(name[0][0] + '. ' + name[1])
    return formatted_names

input_data = [['Launa', 'Withers'], ['Lakenya', 'Edison'], ['Brendan', 'Hage'], ['Bradford', 'Lango'], ['Rudolf', 'Akiyama'], ['Lara', 'Constable']]
output = format_names(input_data)
print(output)
