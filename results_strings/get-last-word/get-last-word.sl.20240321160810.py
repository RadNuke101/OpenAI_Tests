# Prompt: return the last word of the inputted phrase
# Input: ['focus on one thing at a time'] -> Output: time
# Input: ['premature opt is the root of all evil'] -> Output: evil
# Input: ['where is life'] -> Output: life

def last_word(input_phrase):
    words = input_phrase.split()
    return words[-1]

# Test cases
print(last_word('focus on one thing at a time'))  # Output: time
print(last_word('premature opt is the root of all evil'))  # Output: evil
print(last_word('where is life'))  # Output: life
time
evil
life
