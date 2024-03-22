# Prompt: if contains "9999999", return true, else false
# Input: 'dhfjd9999999dfda' 
# Output: true
# Input: 'ddsss999dfdfsfd'
# Output: false

def check_string(input_str):
    if "9999999" in input_str:
        return True
    else:
        return False

# Test cases
print(check_string('dhfjd9999999dfda'))  # Output: True
print(check_string('ddsss999dfdfsfd'))    # Output: False
