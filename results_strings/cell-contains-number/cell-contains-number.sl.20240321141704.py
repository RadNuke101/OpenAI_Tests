# Prompt: if a number is present in the inputted expression, return true, else false
# Input: 'A bird in the hand is worth 2 in the bush.'
# Output: true

def check_for_number(input_str):
    for char in input_str:
        if char.isdigit():
            return 'true'
    return 'false'

# Test cases
print(check_for_number('A bird in the hand is worth 2 in the bush.'))  # Output: true
print(check_for_number('A bird in the hand is worth two in the bush.'))  # Output: false
print(check_for_number('The 15 shortcuts you simply must know'))  # Output: true
true
false
true
