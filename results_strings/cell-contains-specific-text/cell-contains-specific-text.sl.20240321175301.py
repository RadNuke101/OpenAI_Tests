# Prompt: if the second input (word or phrase) is in the first input (expression), return true, else false
# Input: 'An apple a day keeps the doctor away', 'apple'
# Output: true
# Input: 'An apple a day keeps the doctor away', 'orange'
# Output: false
# Input: 'Better the devil you know', 'you know'
# Output: true

def check_word_in_phrase(phrase, word):
    return str(word in phrase)

# Test cases
print(check_word_in_phrase('An apple a day keeps the doctor away', 'apple'))  # Output: true
print(check_word_in_phrase('An apple a day keeps the doctor away', 'orange'))  # Output: false
print(check_word_in_phrase('Better the devil you know', 'you know'))  # Output: true
true
false
true
