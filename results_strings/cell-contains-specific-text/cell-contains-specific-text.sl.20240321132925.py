# Prompt: if the second input (word or phrase) is in the first input (expression), return true, else false
# Input: ['An apple a day keeps the doctor away', 'apple']
# Output: true
# Input: ['An apple a day keeps the doctor away', 'orange']
# Output: false
# Input: ['Better the devil you know', 'you know']
# Output: true

def check_substring(expression, word):
    if word in expression:
        return "true"
    else:
        return "false"

# Test cases
print(check_substring('An apple a day keeps the doctor away', 'apple'))  # Output: true
print(check_substring('An apple a day keeps the doctor away', 'orange'))  # Output: false
print(check_substring('Better the devil you know', 'you know'))  # Output: true
