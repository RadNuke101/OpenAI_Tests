def return_last_three_numbers(input_list):
    output_list = []
    for item in input_list:
        output_list.append(item[0][-3:])
    return output_list

input_list = [['938-242-504'], ['308-916-545'], ['623-599-749'], ['981-424-843'], ['118-980-214'], ['244-655-094']]
print(return_last_three_numbers(input_list))
