def return_last_part(input):
    return [i[0].split('/')[-1] for i in input]

input = [['home/Excel/Sheet1.xls'], ['home/user/Sheet1.xls']]
output = return_last_part(input)
print(output)
