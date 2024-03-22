# Prompt: if both the first and second inputs match exactly, including capitalization, return true, else false
# Input: ['apple', 'apple'] Output: true
# Input: ['orange', 'Orange'] Output: false
# Input: ['peach', 'peach'] Output: true
# Input: ['cherry', 'cherrY'] Output: false

def compare_strings(input1, input2):
    if input1 == input2:
        return True
    else:
        return False

# Test cases
print(compare_strings('apple', 'apple'))  # Output: True
print(compare_strings('orange', 'Orange'))  # Output: False
print(compare_strings('peach', 'peach'))  # Output: True
print(compare_strings('cherry', 'cherrY'))  # Output: False
