def remove_numbers(input_list):
    output = []
    for item in input_list:
        new_item = ''.join([char for char in item[0] if not char.isdigit()])
        output.append(new_item)
    return output

input_list = [['80v', '3'], ['10hrs', '3'], ['7h', '2'], ['500m', '4']]
print(remove_numbers(input_list))
