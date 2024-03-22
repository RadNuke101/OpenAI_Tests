def get_last_part(input_list):
    return [x[0].split('/')[-1] for x in input_list]

# Test the function with the provided input
input_list = [['c=/users/dave/shotcut.xls'], ['c=/users/dave/formulas.xls'], ['c=/users/dave/pivot table.xls']]
output = get_last_part(input_list)
print(output)
