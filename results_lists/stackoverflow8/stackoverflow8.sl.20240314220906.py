def get_last_part(input):
    return [x[0].split('/')[-1] for x in input]

# Test the function
input = [['home/Excel/Sheet1.xls'], ['home/user/Sheet1.xls']]
print(get_last_part(input))  # Output: ['Sheet1.xls', 'Sheet1.xls']
