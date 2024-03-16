def remove_numbers(input_list):
    output_list = [item[0].rstrip('0123456789') for item in input_list]
    return output_list

input_list = [['apples30', '7'], ['peaches24', '8'], ['peaches0', '8'], ['pears', '6']]
print(remove_numbers(input_list))
