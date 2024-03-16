def format_names(names):
    result = []
    for name in names:
        result.append(name[1] + ', ' + name[0][0] + '.')
    return result

input_data = [['Launa', 'Withers'], ['Lakenya', 'Edison'], ['Brendan', 'Hage'], ['Bradford', 'Lango'], ['Rudolf', 'Akiyama']]
output_data = format_names(input_data)
print(output_data)
