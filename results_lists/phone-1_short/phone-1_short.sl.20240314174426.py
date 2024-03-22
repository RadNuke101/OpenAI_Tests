def extract_numbers(input_list):
    output_list = []
    for sublist in input_list:
        numbers = sublist[0].split('-')
        output_list.append(numbers[1])
    return output_list

input_list = [['938-242-504'], ['308-916-545'], ['623-599-749'], ['981-424-843'], ['118-980-214'], ['244-655-094']]
output = extract_numbers(input_list)
print(output)
