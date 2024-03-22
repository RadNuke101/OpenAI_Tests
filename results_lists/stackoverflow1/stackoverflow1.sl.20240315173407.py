def remove_inc(input_list):
    output_list = []
    for item in input_list:
        output_list.append(item[0].split(' Inc')[0])
    return output_list

input_list = [['Trucking Inc.'], ['New Truck Inc'], ['ABV Trucking Inc, LLC']]
output = remove_inc(input_list)
print(output)
