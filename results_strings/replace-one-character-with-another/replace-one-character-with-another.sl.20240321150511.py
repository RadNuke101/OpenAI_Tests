# Prompt: replaces spaces in input with "-", and given input as ['801 456 8756'] output is 801-456-8756, given input as ['978 456 8756'] output is 978-456-8756

def replace_spaces_with_dash(input_str):
    return input_str.replace(" ", "-")

# Test cases
input1 = '801 456 8756'
output1 = '801-456-8756'
print(replace_spaces_with_dash(input1))  # Output: 801-456-8756

input2 = '978 456 8756'
output2 = '978-456-8756'
print(replace_spaces_with_dash(input2))  # Output: 978-456-8756
