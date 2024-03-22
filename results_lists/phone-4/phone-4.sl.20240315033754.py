def replace_dash(input_list):
    output_list = []
    for sublist in input_list:
        for item in sublist:
            output_list.append(item.replace("-", "."))
    return output_list

input_list = [['938-242-504'], ['308-916-545'], ['623-599-749'], ['981-424-843'], ['118-980-214'], ['244-655-094']]
output = replace_dash(input_list)
print(output)
