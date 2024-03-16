def get_last_part(input_list):
    output = []
    for item in input_list:
        output.append(item[0].split('/')[-1])
    return output

input_list = [['c=/users/dave/shotcut.xls'], ['c=/users/dave/formulas.xls'], ['c=/users/dave/pivot table.xls']]
print(get_last_part(input_list))
