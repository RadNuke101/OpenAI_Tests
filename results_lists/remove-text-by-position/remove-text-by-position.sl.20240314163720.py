def get_last_part(input):
    return [x[0].split('/')[-1] for x in input]

input = [['c=/users/dave/shotcut.xls'], ['c=/users/dave/formulas.xls'], ['c=/users/dave/pivot table.xls']]
output = get_last_part(input)
print(output)
