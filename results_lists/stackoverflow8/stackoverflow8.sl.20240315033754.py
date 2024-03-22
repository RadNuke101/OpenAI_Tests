def return_last_part(input):
    return [x[0].split('/')[-1] for x in input]

# Test the function with the given input
input = [['home/Excel/Sheet1.xls'], ['home/user/Sheet1.xls']]
output = return_last_part(input)
print(output)
