# Prompt: return the first word of the inputted phrase
# Input: ['Susan Ann Chang']
# Output: Susan

def first_word(input_phrase):
    # Extract the first word from the input phrase
    first_word = input_phrase.split()[0]
    return first_word

# Test cases
print(first_word('Susan Ann Chang'))  # Output: Susan
print(first_word('Ayako Tanaka'))  # Output: Ayako
print(first_word('Bobby T. smth'))  # Output: Bobby
