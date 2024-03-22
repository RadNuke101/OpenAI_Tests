# Prompt: if both the first and second inputs match exactly, including capitalization, return true, else false
# Input: 'apple', 'apple' => Output: True
# Input: 'orange', 'Orange' => Output: False
# Input: 'peach', 'peach' => Output: True
# Input: 'cherry', 'cherrY' => Output: False

def match_strings(input1, input2):
    return input1 == input2

# Test cases
print(match_strings('apple', 'apple'))  # Output: True
print(match_strings('orange', 'Orange'))  # Output: False
print(match_strings('peach', 'peach'))  # Output: True
print(match_strings('cherry', 'cherrY'))  # Output: False
