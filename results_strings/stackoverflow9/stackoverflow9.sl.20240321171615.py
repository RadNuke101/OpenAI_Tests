# Prompt: return last word/phrase from input
# Input: ['Sarah Jane Jones']
# Output: Jones

def return_last_word(input_list):
    input_str = input_list[0]  # Extract the string from the list
    words = input_str.split()  # Split the string into words
    last_word = words[-1]  # Get the last word
    return last_word

# Test cases
print(return_last_word(['Sarah Jane Jones']))  # Output: Jones
print(return_last_word(['Bob Jane Smithfield']))  # Output: Smithfield
