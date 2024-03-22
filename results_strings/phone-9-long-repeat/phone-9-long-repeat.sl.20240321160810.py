# Prompt: return input, but remove the "+", add a "." in empty space, and replace all "-" with a "."
# Input: ['+45 095-746-635']
# Output: '45.095.746.635'

def format_phone_number(input):
    input_str = input[0].replace("+", "").replace(" ", ".").replace("-", ".")
    return input_str

# Test the function with the given input
input = ['+45 095-746-635']
output = format_phone_number(input)
print(output)
