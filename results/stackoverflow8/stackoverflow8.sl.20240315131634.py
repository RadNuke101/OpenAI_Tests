def return_last_element(input_list):
    output_list = []
    for item in input_list:
        output_list.append(item[0].split('/')[-1])
    return output_list

input_list = [['home/Excel/Sheet1.xls'], ['home/user/Sheet1.xls']]
print(return_last_element(input_list))
