def combine_names(input_list):
    return [f"{item[0]} {item[1]}" for item in input_list]

# Test the function
input_list = [['susan', 'chang'], ['aaron', 'kim']]
print(combine_names(input_list))
