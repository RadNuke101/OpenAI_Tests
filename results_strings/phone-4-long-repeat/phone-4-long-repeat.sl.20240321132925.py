# Prompt: return input, but replace "-" with ".", and given input as ['938-242-504'] output is 938.242.504

def replace_dash_with_dot(input_str):
    return input_str.replace("-", ".")

# Test cases
print(replace_dash_with_dot('938-242-504'))  # Output: 938.242.504
print(replace_dash_with_dot('308-916-545'))  # Output: 308.916.545
print(replace_dash_with_dot('623-599-749'))  # Output: 623.599.749
print(replace_dash_with_dot('981-424-843'))  # Output: 981.424.843
print(replace_dash_with_dot('118-980-214'))  # Output: 118.980.214
print(replace_dash_with_dot('244-655-094'))  # Output: 244.655.094
print(replace_dash_with_dot('830-941-991'))  # Output: 830.941.991
print(replace_dash_with_dot('911-186-562'))  # Output: 911.186.562
print(replace_dash_with_dot('002-500-200'))  # Output: 002.500.200
print(replace_dash_with_dot('113-860-034'))  # Output: 113.860.034
print(replace_dash_with_dot('457-622-959'))  # Output: 457.622.959
print(replace_dash_with_dot('986-722-311'))  # Output: 986.722.311
print(replace_dash_with_dot('110-170-771'))  # Output: 110.170.771
print(replace_dash_with_dot('469-610-118'))  # Output: 469.610.118
print(replace_dash_with_dot('817-925-247'))  # Output: 817.925.247
print(replace_dash_with_dot('256-899-439'))  # Output: 256.899.439
print(replace_dash_with_dot('886-911-726'))  # Output: 886.911.726
print(replace_dash_with_dot('562-950-358'))  # Output: 562.950.358
print(replace_dash_with_dot('693-049-588'))  # Output: 693.049.588
print(replace_dash_with_dot('840-503-234'))  # Output: 840.503.234
