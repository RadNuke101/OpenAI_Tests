def format_names(names):
    result = []
    for name in names:
        first_initial = name[0][0]
        formatted_name = f"{first_initial}. {name[1]}"
        result.append(formatted_name)
    return result

input_names = [['Launa', 'Withers'], ['Lakenya', 'Edison'], ['Brendan', 'Hage'], ['Bradford', 'Lango'], ['Rudolf', 'Akiyama'], ['Lara', 'Constable']]
output_names = format_names(input_names)
print(output_names)
