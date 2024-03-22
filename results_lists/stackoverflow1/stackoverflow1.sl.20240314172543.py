def remove_suffix(input_list):
    output_list = []
    for item in input_list:
        name = item[0].split(' Inc')[0]
        output_list.append(name)
    return output_list

input_list = [['Trucking Inc.'], ['New Truck Inc'], ['ABV Trucking Inc, LLC']]
output = remove_suffix(input_list)
print(output)
