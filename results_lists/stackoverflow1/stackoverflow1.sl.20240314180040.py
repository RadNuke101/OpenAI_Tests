def remove_suffix(input_list):
    output = []
    for item in input_list:
        name = item[0].split(' ')[0]
        output.append(name)
    return output

input_list = [['Trucking Inc.'], ['New Truck Inc'], ['ABV Trucking Inc, LLC']]
print(remove_suffix(input_list))
