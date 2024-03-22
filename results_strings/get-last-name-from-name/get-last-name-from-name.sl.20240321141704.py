# Prompt: return the second word of the inputted phrase
# Input: ['Park Kim']
# Output: Kim

def second_word(input_phrase):
    words = input_phrase.split()
    if len(words) >= 2:
        return words[1]
    else:
        return "No second word found"

# Test cases
print(second_word('Park Kim'))  # Output: Kim
print(second_word('Lee Kim'))  # Output: Kim
print(second_word('Kim Lee'))  # Output: Lee
