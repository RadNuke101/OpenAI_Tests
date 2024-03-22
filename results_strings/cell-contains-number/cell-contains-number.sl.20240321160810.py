# Prompt: if a number is present in the inputted expression, return true, else false
# Input: 'A bird in the hand is worth 2 in the bush.' 
# Output: 'true'
# Input: 'A bird in the hand is worth two in the bush.' 
# Output: 'false'
# Input: 'The 15 shortcuts you simply must know' 
# Output: 'true'

def check_number_presence(input_str):
    for char in input_str:
        if char.isdigit():
            return 'true'
    return 'false'

# Test cases
print(check_number_presence('A bird in the hand is worth 2 in the bush.'))  # Output: 'true'
print(check_number_presence('A bird in the hand is worth two in the bush.'))  # Output: 'false'
print(check_number_presence('The 15 shortcuts you simply must know'))  # Output: 'true'
