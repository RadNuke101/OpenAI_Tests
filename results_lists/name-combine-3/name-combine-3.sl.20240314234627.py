def format_names(names):
    result = []
    for name in names:
        first_letter = name[0][0]
        formatted_name = f"{first_letter}. {name[1]}"
        result.append(formatted_name)
    return result

input_data = [['Launa', 'Withers'], ['Lakenya', 'Edison'], ['Brendan', 'Hage'], ['Bradford', 'Lango'], ['Rudolf', 'Akiyama'], ['Lara', 'Constable']]
output = format_names(input_data)
print(output)
