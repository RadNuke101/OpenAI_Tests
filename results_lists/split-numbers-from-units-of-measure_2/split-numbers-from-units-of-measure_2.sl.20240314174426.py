def remove_numbers(input_list):
    output_list = []
    for item in input_list:
        output_list.append(''.join([char for char in item[0] if not char.isdigit()]))
    return output_list

input_list = [['80v', '3'], ['10hrs', '3'], ['7h', '2'], ['500m', '4']]
print(remove_numbers(input_list))
