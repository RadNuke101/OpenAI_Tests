def format_names(names):
    formatted_names = []
    for name in names:
        first_letter = name[0][0]
        formatted_name = f"{first_letter}. {name[1]}"
        formatted_names.append(formatted_name)
    return formatted_names

input_data = [['Launa', 'Withers'], ['Lakenya', 'Edison'], ['Brendan', 'Hage'], ['Bradford', 'Lango'], ['Rudolf', 'Akiyama'], ['Lara', 'Constable']]
output = format_names(input_data)
print(output)
