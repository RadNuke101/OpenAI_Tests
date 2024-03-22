def find_position(input_str, num):
    if num == '1':
        return input_str.index('_') + 1
    elif num == '2':
        return input_str.index('_', input_str.index('_') + 1) + 1
    elif num == '3':
        return input_str.rindex('_') + 1

# Prompt: if second input (second column) is "1", return the position of the first "_", else if second input is "2", return the position of the second "_", else if second input is "3", return the position of the third "_"
# Input: ['replies to _aya, _tasisuke, and _chan', '1']
# Output: 12
# Input: ['replies to _aya, _tasisuke, and _chan', '2']
# Output: 18
# Input: ['replies to _aya, _tasisuke, and _chan', '3']
# Output: 33

# Test the function with the provided inputs
print(find_position('replies to _aya, _tasisuke, and _chan', '1'))  # Output: 12
print(find_position('replies to _aya, _tasisuke, and _chan', '2'))  # Output: 18
print(find_position('replies to _aya, _tasisuke, and _chan', '3'))  # Output: 33
