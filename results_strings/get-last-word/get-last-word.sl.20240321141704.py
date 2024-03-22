# Prompt: return the last word of the inputted phrase
# Input: ['focus on one thing at a time']
# Output: time

def return_last_word(input_phrase):
    words = input_phrase.split()
    return words[-1]

# Test cases
print(return_last_word('focus on one thing at a time'))  # Output: time
print(return_last_word('premature opt is the root of all evil'))  # Output: evil
print(return_last_word('where is life'))  # Output: life
