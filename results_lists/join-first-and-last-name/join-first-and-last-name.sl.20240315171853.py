def combine_names(input_list):
    return [f'{item[0]} {item[1]}' for item in input_list]

input_list = [['susan', 'chang'], ['aaron', 'kim']]
output = combine_names(input_list)
print(output)
