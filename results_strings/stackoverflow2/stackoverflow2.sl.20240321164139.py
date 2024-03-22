# Prompt: remove the last word/phrase from input
# Input: ['india china japan']
# Output: india china

def remove_last_word(input_str):
    words = input_str.split()
    output_str = ' '.join(words[:-1])
    return output_str

# Test cases
print(remove_last_word('india china japan'))  # Output: india china
print(remove_last_word('indonesia korea'))     # Output: indonesia
