# Prompt: remove all instances of "-" from input
# Input: ['801-345-1987']
# Output: 8013451987
# Input: ['612-554-2000']
# Output: 6125542000

def remove_dashes(input_str):
    return input_str.replace("-", "")

# Test cases
print(remove_dashes('801-345-1987'))  # Output: 8013451987
print(remove_dashes('612-554-2000'))  # Output: 6125542000
