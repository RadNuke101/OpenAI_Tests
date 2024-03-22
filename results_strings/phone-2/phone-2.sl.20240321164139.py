# Prompt: return the last three numbers
# Input: '938-242-504'
# Output: '504'

def return_last_three_numbers(input_str):
    return input_str[-3:]

# Test cases
print(return_last_three_numbers('938-242-504'))  # Output: '504'
print(return_last_three_numbers('308-916-545'))  # Output: '545'
print(return_last_three_numbers('623-599-749'))  # Output: '749'
print(return_last_three_numbers('981-424-843'))  # Output: '843'
print(return_last_three_numbers('118-980-214'))  # Output: '214'
print(return_last_three_numbers('244-655-094'))  # Output: '094'
