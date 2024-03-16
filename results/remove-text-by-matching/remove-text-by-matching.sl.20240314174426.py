def remove_dashes(input_list):
    output_list = []
    for sublist in input_list:
        output_list.append(sublist[0].replace('-', ''))
    return output_list

# Test the function with the provided input
input_list = [['801-345-1987'], ['612-554-2000']]
output = remove_dashes(input_list)
print(output)
