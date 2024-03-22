# Prompt: if contains "9999999", return true, else false
# Input: 'dhfjd9999999dfda'
# Output: true

def check_string(input_str):
    if "9999999" in input_str:
        return "true"
    else:
        return "false"

# Test cases
print(check_string('dhfjd9999999dfda'))  # true
print(check_string('ddsss999dfdfsfd'))    # false
