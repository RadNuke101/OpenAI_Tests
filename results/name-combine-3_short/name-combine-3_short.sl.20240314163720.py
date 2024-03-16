def format_names(names):
    result = []
    for name in names:
        result.append(name[0][0] + '. ' + name[1])
    return result

input_names = [['Launa', 'Withers'], ['Lakenya', 'Edison'], ['Brendan', 'Hage'], ['Bradford', 'Lango'], ['Rudolf', 'Akiyama'], ['Lara', 'Constable']]
output_names = format_names(input_names)
print(output_names)
