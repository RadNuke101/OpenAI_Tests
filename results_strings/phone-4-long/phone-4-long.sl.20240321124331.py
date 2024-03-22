def replace_dash_with_dot(input_str):
    return input_str.replace("-", ".")

# Prompt: return input, but replace "-" with "."
# Input: ['938-242-504']
# Output: 938.242.504

input_str = '938-242-504'
output_str = replace_dash_with_dot(input_str)
print(output_str)  # Output: 938.242.504
