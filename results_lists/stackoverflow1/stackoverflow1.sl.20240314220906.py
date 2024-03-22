def remove_inc(input_list):
    output_list = []
    for item in input_list:
        name = item[0]
        if 'Inc' in name:
            name = name.split('Inc')[0].strip()
        output_list.append(name)
    return output_list

input_list = [['Trucking Inc.'], ['New Truck Inc'], ['ABV Trucking Inc, LLC']]
output = remove_inc(input_list)
print(output)
