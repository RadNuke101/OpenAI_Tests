# Prompt: replaces spaces in input with "-", and given input as ['801 456 8756'] output is 801-456-8756, given input as ['978 456 8756'] output is 978-456-8756

def replace_spaces_with_dash(input_str):
    output_str = input_str.replace(" ", "-")
    return output_str

# Test cases
print(replace_spaces_with_dash('801 456 8756'))  # Output: 801-456-8756
print(replace_spaces_with_dash('978 456 8756'))  # Output: 978-456-8756
