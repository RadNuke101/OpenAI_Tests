def format_names(input_list):
    output_list = []
    for names in input_list:
        first_initial = names[0][0]
        formatted_name = first_initial + '. ' + names[1]
        output_list.append(formatted_name)
    return output_list

input_list = [['Launa', 'Withers'], ['Lakenya', 'Edison'], ['Brendan', 'Hage'], ['Bradford', 'Lango'], ['Rudolf', 'Akiyama'], ['Lara', 'Constable']]
print(format_names(input_list))
