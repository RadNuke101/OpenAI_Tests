def format_names(input_list):
    output_list = []
    for names in input_list:
        output_list.append(names[0][0] + '. ' + names[1])
    return output_list

input_list = [['Launa', 'Withers'], ['Lakenya', 'Edison'], ['Brendan', 'Hage'], ['Bradford', 'Lango'], ['Rudolf', 'Akiyama'], ['Lara', 'Constable']]
print(format_names(input_list))
