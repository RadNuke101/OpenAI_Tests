def replace_dash(input_str):
    return input_str.replace("-", ".")

# Prompt: return input, but replace "-" with "."
# Given input as ['938-242-504'] output is 938.242.504
# Given input as ['308-916-545'] output is 308.916.545
# Given input as ['623-599-749'] output is 623.599.749
# ...

# Test cases
print(replace_dash('938-242-504'))  # Output: 938.242.504
print(replace_dash('308-916-545'))  # Output: 308.916.545
print(replace_dash('623-599-749'))  # Output: 623.599.749
