# Prompt: return last word/phrase from input
# Input: ['Sarah Jane Jones']
# Output: Jones

def return_last_word(input_str):
    words = input_str.split()
    return words[-1]

# Test cases
print(return_last_word('Sarah Jane Jones'))  # Output: Jones
print(return_last_word('Bob Jane Smithfield'))  # Output: Smithfield
