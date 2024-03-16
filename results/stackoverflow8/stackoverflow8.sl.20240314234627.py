def return_last_element(input_list):
    return [x[0].split("/")[-1] for x in input_list]

# Test the function with the given input
input_list = [['home/Excel/Sheet1.xls'], ['home/user/Sheet1.xls']]
print(return_last_element(input_list))
