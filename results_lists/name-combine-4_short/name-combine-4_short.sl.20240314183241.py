def format_names(input_list):
    output_list = []
    for names in input_list:
        last_name = names[1]
        first_name = names[0]
        formatted_name = last_name + ', ' + first_name[0] + '.'
        output_list.append(formatted_name)
    return output_list

input_list = [['Launa', 'Withers'], ['Lakenya', 'Edison'], ['Brendan', 'Hage'], ['Bradford', 'Lango'], ['Rudolf', 'Akiyama']]
output = format_names(input_list)
print(output)
