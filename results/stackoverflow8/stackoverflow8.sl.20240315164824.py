def get_last_part(input_list):
    output = []
    for item in input_list:
        output.append(item[0].split('/')[-1])
    return output

# Test the function
input_list = [['home/Excel/Sheet1.xls'], ['home/user/Sheet1.xls']]
print(get_last_part(input_list))  # Output: ['Sheet1.xls', 'Sheet1.xls']
