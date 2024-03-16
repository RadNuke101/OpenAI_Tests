def combine_names(input_list):
    return [name[0] + ' ' + name[1] for name in input_list]

input_list = [['susan', 'chang'], ['aaron', 'kim']]
output = combine_names(input_list)
print(output)
