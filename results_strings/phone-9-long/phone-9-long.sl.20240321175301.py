def format_phone_number(input):
    input = input[1:-1]  # remove brackets
    input = input.replace("+", "").replace("-", "").replace(" ", ".")  # format the phone number
    return input

# Prompt: return input, but remove the "+", add a "." in empty space, and replace all "-" with a "."
# Input: ['+45 095-746-635']
# Output: '45.095.746.635'

# Test the function
print(format_phone_number('+45 095-746-635'))  # Output: '45.095.746.635'
