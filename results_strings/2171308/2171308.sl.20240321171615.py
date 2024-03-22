# Prompt: return first letter of first word, followed by a space, and then the second word
# Input: ['John Doe'] Output: J Doe
# Input: ['Mayur Naik'] Output: M Naik
# Input: ['Nimit Singh'] Output: N Singh

def format_name(input_str):
    words = input_str.split()
    return words[0][0] + " " + words[1]

# Test cases
print(format_name('John Doe'))  # Output: J Doe
print(format_name('Mayur Naik'))  # Output: M Naik
print(format_name('Nimit Singh'))  # Output: N Singh
J Doe
M Naik
N Singh
