# Prompt: remove all instances of "-" from input
# Input: ['801-345-1987']
# Output: 8013451987

def remove_dash(input_str):
    return input_str.replace("-", "")

# Test cases
print(remove_dash('801-345-1987'))  # Output: 8013451987
print(remove_dash('612-554-2000'))  # Output: 6125542000
