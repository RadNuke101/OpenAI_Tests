def get_last_part(input_list):
    return [x[0].split('/')[-1] for x in input_list]

# Test the function
input_list = [['home/Excel/Sheet1.xls'], ['home/user/Sheet1.xls']]
print(get_last_part(input_list))  # Output: ['Sheet1.xls', 'Sheet1.xls']
