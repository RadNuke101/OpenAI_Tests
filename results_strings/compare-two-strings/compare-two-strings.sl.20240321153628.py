# Prompt: if both the first and second inputs match exactly, including capitalization, return true, else false
# Input: ['apple', 'apple'] Output: true
# Input: ['orange', 'Orange'] Output: false
# Input: ['peach', 'peach'] Output: true
# Input: ['cherry', 'cherrY'] Output: false

def check_inputs(input1, input2):
    return input1 == input2

# Test cases
print(check_inputs('apple', 'apple'))  # Output: True
print(check_inputs('orange', 'Orange'))  # Output: False
print(check_inputs('peach', 'peach'))  # Output: True
print(check_inputs('cherry', 'cherrY'))  # Output: False
