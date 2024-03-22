def rearrange_names(input_list):
    output_list = []
    for names in input_list:
        output_list.append(names[1] + ' ' + names[0])
    return output_list

input_list = [['Launa', 'Withers'], ['Lakenya', 'Edison'], ['Brendan', 'Hage'], ['Bradford', 'Lango'], ['Rudolf', 'Akiyama'], ['Lara', 'Constable']]
print(rearrange_names(input_list))
