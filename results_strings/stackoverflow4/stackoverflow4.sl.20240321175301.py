# Prompt: Given input as ['R/V<208,0,32>'] output is R/V 208 0 32, given input as ['R/S<184,28,16>'] output is R/S 184 28 16, given input as ['R/B<255,88,80>'] output is R/B 255 88 80

def replace_chars(input_str):
    input_str = input_str.replace("<", " ").replace(">", " ").replace(",", " ")
    return input_str

# Test cases
print(replace_chars('R/V<208,0,32>'))  # Output: R/V 208 0 32
print(replace_chars('R/S<184,28,16>'))  # Output: R/S 184 28 16
print(replace_chars('R/B<255,88,80>'))  # Output: R/B 255 88 80
