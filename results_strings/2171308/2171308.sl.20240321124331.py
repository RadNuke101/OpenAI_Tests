# Prompt: return first letter of first word, followed by a space, and then the second word
# Input: ['John Doe'] Output: J Doe
# Input: ['Mayur Naik'] Output: M Naik
# Input: ['Nimit Singh'] Output: N Singh

def process_names(input_list):
    input_str = input_list[0]
    words = input_str.split()
    
    output = words[0][0] + " " + words[1]
    
    return output

# Test cases
print(process_names(['John Doe']))  # Output: J Doe
print(process_names(['Mayur Naik']))  # Output: M Naik
print(process_names(['Nimit Singh']))  # Output: N Singh
