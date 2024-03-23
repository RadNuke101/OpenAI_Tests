# Prompt: return the first word of the inputted phrase
# Input: ['Susan Ann Chang'] -> Output: 'Susan'
# Input: ['Ayako Tanaka'] -> Output: 'Ayako'
# Input: ['Bobby T. smth'] -> Output: 'Bobby'

def first_word(input_phrase):
    return input_phrase.split()[0]

# Test cases
print(first_word('Susan Ann Chang'))  # Output: 'Susan'
print(first_word('Ayako Tanaka'))  # Output: 'Ayako'
print(first_word('Bobby T. smth'))  # Output: 'Bobby'