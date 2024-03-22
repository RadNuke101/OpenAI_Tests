# Prompt: if contains "9999999", return true, else false
# Input: 'dhfjd9999999dfda'
# Output: true

def check_for_pattern(input_str):
    if "9999999" in input_str:
        return "true"
    else:
        return "false"

# Test cases
print(check_for_pattern('dhfjd9999999dfda'))  # Output: true
print(check_for_pattern('ddsss999dfdfsfd'))  # Output: false
