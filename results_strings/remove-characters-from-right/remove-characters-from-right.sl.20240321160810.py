# Prompt: delete "miles" from input
# Input: ['736 miles'], Output: 736
# Input: ['1255 miles'], Output: 1255
# Input: ['1221 miles'], Output: 1221
# Input: ['790 miles'], Output: 790

def extract_miles(input_str):
    return int(input_str.replace(" miles", ""))

# Test cases
print(extract_miles('736 miles'))  # Output: 736
print(extract_miles('1255 miles'))  # Output: 1255
print(extract_miles('1221 miles'))  # Output: 1221
print(extract_miles('790 miles'))  # Output: 790
