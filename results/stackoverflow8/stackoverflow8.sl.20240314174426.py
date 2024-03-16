def return_after_last_slash(input_list):
    output_list = []
    for item in input_list:
        output_list.append(item[0].split('/')[-1])
    return output_list

input_list = [['home/Excel/Sheet1.xls'], ['home/user/Sheet1.xls']]
print(return_after_last_slash(input_list))  # Output: ['Sheet1.xls', 'Sheet1.xls']
