def remove_numbers(input_list):
    output_list = []
    for sublist in input_list:
        for item in sublist:
            if not item.isdigit():
                output_list.append(item)
                break
    return output_list

input_list = [['80v', '3'], ['10hrs', '3'], ['7h', '2'], ['500m', '4']]
print(remove_numbers(input_list))
