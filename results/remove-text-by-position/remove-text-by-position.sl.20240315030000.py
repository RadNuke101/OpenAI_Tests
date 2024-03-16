def return_last_part(input_list):
    output_list = []
    for item in input_list:
        output_list.append(item[0].split('/')[-1])
    return output_list

input_list = [['c=/users/dave/shotcut.xls'], ['c=/users/dave/formulas.xls'], ['c=/users/dave/pivot table.xls']]
output = return_last_part(input_list)
print(output)
