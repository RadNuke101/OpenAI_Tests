def first_last_name(input_str):
    # Prompt: return first letter of first word, followed by a space, and then the second word
    # Input: ['John Doe'] -> Output: J Doe
    # Input: ['Mayur Naik'] -> Output: M Naik
    # Input: ['Nimit Singh'] -> Output: N Singh
    
    # Extract the first and last name from the input string
    first_name, last_name = input_str.split()
    
    # Construct the output string
    output_str = first_name[0] + " " + last_name
    
    return output_str

# Test cases
print(first_last_name('John Doe'))  # Output: J Doe
print(first_last_name('Mayur Naik'))  # Output: M Naik
print(first_last_name('Nimit Singh'))  # Output: N Singh
