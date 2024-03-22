# Prompt: in input, replace "<", ">", and all commas with a space
# Input: 'R/V<208,0,32>'
# Output: 'R/V 208 0 32'

def replace_chars(input_str):
    output_str = input_str.replace('<', ' ').replace('>', ' ').replace(',', ' ')
    return output_str

# Test cases
print(replace_chars('R/V<208,0,32>'))  # Output: 'R/V 208 0 32'
print(replace_chars('R/S<184,28,16>'))  # Output: 'R/S 184 28 16'
print(replace_chars('R/B<255,88,80>'))  # Output: 'R/B 255 88 80'
R/V 208 0 32
R/S 184 28 16
R/B 255 88 80
