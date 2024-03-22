# Prompt: delete "miles" from input
# Input: ['736 miles']
# Output: 736

def remove_miles(input_str):
    return int(input_str.replace(" miles", ""))

# Test cases
print(remove_miles('736 miles'))  # Output: 736
print(remove_miles('1255 miles'))  # Output: 1255
print(remove_miles('1221 miles'))  # Output: 1221
print(remove_miles('790 miles'))  # Output: 790
