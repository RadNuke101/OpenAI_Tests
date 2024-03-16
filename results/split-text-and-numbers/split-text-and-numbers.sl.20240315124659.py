def remove_numbers(input_list):
    output_list = []
    for item in input_list:
        output_list.append(''.join([char for char in item[0] if not char.isdigit()]))
    return output_list

input_list = [['apples30', '7'], ['peaches24', '8'], ['peaches0', '8'], ['pears', '6']]
print(remove_numbers(input_list))
