# Prompt: return the text between "<" and ">" in the inputted expression
# Input: 'Jones <60>'
# Output: '60'

def extract_text(input_str):
    start = input_str.find("<") + 1
    end = input_str.find(">")
    return input_str[start:end]

# Test cases
print(extract_text('Jones <60>'))  # Output: '60'
print(extract_text('Jones <57>'))  # Output: '57'
print(extract_text('Jones <55>'))  # Output: '55'
