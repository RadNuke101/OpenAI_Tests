def combine_names(input):
    return [f"{name[0]} {name[1]}" for name in input]

input = [['susan', 'chang'], ['aaron', 'kim']]
output = combine_names(input)
print(output)
