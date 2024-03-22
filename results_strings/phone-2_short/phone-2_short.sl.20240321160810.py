# Prompt: return the last three numbers
# Input: '938-242-504', Output: '504'
# Input: '308-916-545', Output: '545'
# Input: '623-599-749', Output: '749'
# Input: '981-424-843', Output: '843'
# Input: '118-980-214', Output: '214'
# Input: '244-655-094', Output: '094'

def get_last_three_numbers(input_str):
    return input_str[-3:]

# Test cases
print(get_last_three_numbers('938-242-504'))  # Output: '504'
print(get_last_three_numbers('308-916-545'))  # Output: '545'
print(get_last_three_numbers('623-599-749'))  # Output: '749'
print(get_last_three_numbers('981-424-843'))  # Output: '843'
print(get_last_three_numbers('118-980-214'))  # Output: '214'
print(get_last_three_numbers('244-655-094'))  # Output: '094'
