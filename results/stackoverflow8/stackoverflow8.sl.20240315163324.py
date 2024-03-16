def return_last_part(input):
    output = []
    for item in input:
        output.append(item[0].split('/')[-1])
    return output

input = [['home/Excel/Sheet1.xls'], ['home/user/Sheet1.xls']]
print(return_last_part(input))
