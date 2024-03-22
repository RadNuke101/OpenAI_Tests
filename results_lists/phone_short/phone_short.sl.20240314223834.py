def return_first_three_numbers(input_list):
    output = [x[0][:3] for x in input_list]
    return output

input_list = [['938-242-504'], ['308-916-545'], ['623-599-749'], ['981-424-843'], ['118-980-214'], ['244-655-094']]
print(return_first_three_numbers(input_list))
