# Prompt: if both the first and second inputs match exactly, including capitalization, return true, else false
# Input: ['apple', 'apple'] 
# Output: true
# Input: ['orange', 'Orange'] 
# Output: false
# Input: ['peach', 'peach'] 
# Output: true
# Input: ['cherry', 'cherrY'] 
# Output: false

def match_strings(input1, input2):
    return input1 == input2

# Test cases
print(match_strings('apple', 'apple'))  # Output: true
print(match_strings('orange', 'Orange'))  # Output: false
print(match_strings('peach', 'peach'))  # Output: true
print(match_strings('cherry', 'cherrY'))  # Output: false
