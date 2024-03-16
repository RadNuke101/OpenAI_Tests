def remove_numbers(input_list):
    output_list = []
    for pair in input_list:
        output_list.append(pair[0].rstrip('0123456789'))
    return output_list

input_list = [['apples30', '7'], ['peaches24', '8'], ['peaches0', '8'], ['pears', '6']]
print(remove_numbers(input_list))
