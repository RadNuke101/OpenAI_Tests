# Prompt: return first letter of first word, followed by a space, and then the second word
# Input: ['John Doe'] Output: J Doe
# Input: ['Mayur Naik'] Output: M Naik
# Input: ['Nimit Singh'] Output: N Singh

def first_letter_last_name(input_str):
    words = input_str.split()
    return words[0][0] + " " + words[1]

# Test cases
print(first_letter_last_name('John Doe'))  # Output: J Doe
print(first_letter_last_name('Mayur Naik'))  # Output: M Naik
print(first_letter_last_name('Nimit Singh'))  # Output: N Singh
