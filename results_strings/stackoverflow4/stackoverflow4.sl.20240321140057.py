# Prompt: in input, replace "<", ">", and all commas with a space
# Input: ['R/V<208,0,32>'] Output: R/V 208 0 32
# Input: ['R/S<184,28,16>'] Output: R/S 184 28 16
# Input: ['R/B<255,88,80>'] Output: R/B 255 88 80

def process_input(input_str):
    input_str = input_str.replace("<", " ").replace(">", " ").replace(",", " ")
    return input_str

# Test the function with the given inputs
print(process_input('R/V<208,0,32>'))  # Output: R/V 208 0 32
print(process_input('R/S<184,28,16>'))  # Output: R/S 184 28 16
print(process_input('R/B<255,88,80>'))  # Output: R/B 255 88 80
R/V 208 0 32
R/S 184 28 16
R/B 255 88 80
