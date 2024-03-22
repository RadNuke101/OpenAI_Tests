# Prompt: in input, replace "<", ">", and all commas with a space
# Given input as ['R/V<208,0,32>'] output is R/V 208 0 32
# Given input as ['R/S<184,28,16>'] output is R/S 184 28 16
# Given input as ['R/B<255,88,80>'] output is R/B 255 88 80

def process_input(input_str):
    input_str = input_str.replace("<", " ").replace(">", " ").replace(",", " ")
    return input_str

# Test cases
print(process_input('R/V<208,0,32>'))  # Output: R/V 208 0 32
print(process_input('R/S<184,28,16>'))  # Output: R/S 184 28 16
print(process_input('R/B<255,88,80>'))  # Output: R/B 255 88 80
R/V 208 0 32
R/S 184 28 16
R/B 255 88 80
