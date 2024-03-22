def replace_dash_with_dot(input_str):
    return input_str.replace("-", ".")

# Prompt: return input, but replace "-" with "."
# Input: ['938-242-504']
# Output: 938.242.504
print(replace_dash_with_dot('938-242-504')) 

# Input: ['308-916-545']
# Output: 308.916.545
print(replace_dash_with_dot('308-916-545'))

# Input: ['623-599-749']
# Output: 623.599.749
print(replace_dash_with_dot('623-599-749'))

# Add more test cases if needed
