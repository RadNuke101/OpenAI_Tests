def replace_dash_with_dot(input_str):
    return input_str.replace("-", ".")

# Prompt: return input, but replace "-" with "."
# Input: ['938-242-504']
# Output: 938.242.504

# Test cases
print(replace_dash_with_dot('938-242-504'))  # Output: 938.242.504
print(replace_dash_with_dot('308-916-545'))  # Output: 308.916.545
print(replace_dash_with_dot('623-599-749'))  # Output: 623.599.749
print(replace_dash_with_dot('981-424-843'))  # Output: 981.424.843
print(replace_dash_with_dot('118-980-214'))  # Output: 118.980.214
938.242.504
308.916.545
623.599.749
981.424.843
118.980.214
