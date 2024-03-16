def get_last_part(input_list):
    output = []
    for item in input_list:
        output.append(item[0].split('/')[-1])
    return output

input_list = [['home/Excel/Sheet1.xls'], ['home/user/Sheet1.xls']]
print(get_last_part(input_list))
