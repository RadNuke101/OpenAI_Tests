def combine_names(input_list):
    output = []
    for pair in input_list:
        output.append(' '.join(pair))
    return output

input_list = [['susan', 'chang'], ['aaron', 'kim']]
print(combine_names(input_list))
