def format_names(names):
    formatted_names = []
    for name in names:
        first_initial = name[0][0]
        formatted_name = f"{first_initial}. {name[1]}"
        formatted_names.append(formatted_name)
    return formatted_names

input_names = [['Launa', 'Withers'], ['Lakenya', 'Edison'], ['Brendan', 'Hage'], ['Bradford', 'Lango'], ['Rudolf', 'Akiyama'], ['Lara', 'Constable']]
output_names = format_names(input_names)
print(output_names)
