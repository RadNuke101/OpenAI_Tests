# Prompt: return first letter of first word, followed by a space, and then the second word
# Input: ['John Doe'] Output: J Doe
# Input: ['Mayur Naik'] Output: M Naik
# Input: ['Nimit Singh'] Output: N Singh

def process_input(input_str):
    words = input_str.split()
    output = words[0][0] + " " + words[1]
    return output

# Test cases
print(process_input('John Doe'))  # Output: J Doe
print(process_input('Mayur Naik'))  # Output: M Naik
print(process_input('Nimit Singh'))  # Output: N Singh
