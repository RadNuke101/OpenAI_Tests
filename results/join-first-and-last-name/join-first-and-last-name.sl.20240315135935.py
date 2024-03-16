def combine_names(input_list):
    return [f"{x[0]} {x[1]}" for x in input_list]

input_list = [['susan', 'chang'], ['aaron', 'kim']]
output = combine_names(input_list)
print(output)
