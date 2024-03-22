def format_names(names):
    formatted_names = []
    for name in names:
        formatted_name = name[1] + ', ' + name[0][0] + '.'
        formatted_names.append(formatted_name)
    return formatted_names

input_names = [['Launa', 'Withers'], ['Lakenya', 'Edison'], ['Brendan', 'Hage'], ['Bradford', 'Lango'], ['Rudolf', 'Akiyama']]
output_names = format_names(input_names)
print(output_names)
