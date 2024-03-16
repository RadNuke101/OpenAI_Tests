def combine_names(input_list):
    return [f'{x[0]} {x[1]}' for x in input_list]

# Test the function with the provided input
input_list = [['susan', 'chang'], ['aaron', 'kim']]
output = combine_names(input_list)
print(output)
