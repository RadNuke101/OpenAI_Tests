# Prompt: return first letter of first word, followed by a space, and then the second word
# Input: ['John Doe'] Output: J Doe
# Input: ['Mayur Naik'] Output: M Naik
# Input: ['Nimit Singh'] Output: N Singh

def process_names(input_str):
    names = input_str.split()
    output = names[0][0] + " " + names[1]
    return output

# Test cases
print(process_names('John Doe'))  # Output: J Doe
print(process_names('Mayur Naik'))  # Output: M Naik
print(process_names('Nimit Singh'))  # Output: N Singh
J Doe
M Naik
N Singh
