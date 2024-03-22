def combine_names(input_list):
    return [' '.join(names) for names in input_list]

input_list = [['susan', 'chang'], ['aaron', 'kim']]
output = combine_names(input_list)
print(output)
