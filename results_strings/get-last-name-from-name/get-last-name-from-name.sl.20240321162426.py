# Prompt: return the second word of the inputted phrase
# Input: ['Park Kim'] 
# Output: Kim
# Input: ['Lee Kim'] 
# Output: Kim
# Input: ['Kim Lee'] 
# Output: Lee

def get_second_word(input_phrase):
    words = input_phrase.split()
    return words[1]

# Test cases
print(get_second_word('Park Kim'))  # Output: Kim
print(get_second_word('Lee Kim'))  # Output: Kim
print(get_second_word('Kim Lee'))  # Output: Lee
