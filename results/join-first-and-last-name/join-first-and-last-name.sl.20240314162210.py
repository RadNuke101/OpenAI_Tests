def combine_names(input_list):
    return [f"{name[0]} {name[1]}" for name in input_list]

# Test the function with the given input
input_list = [['susan', 'chang'], ['aaron', 'kim']]
output = combine_names(input_list)
print(output)
