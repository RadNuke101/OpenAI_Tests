def return_last_part(input_list):
    return [x[0].split('/')[-1] for x in input_list]

# Test the function
input_list = [['c=/users/dave/shotcut.xls'], ['c=/users/dave/formulas.xls'], ['c=/users/dave/pivot table.xls']]
print(return_last_part(input_list))
