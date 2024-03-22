# Prompt: return input with parentheses around the first three numbers and delete the first "-" and replace it with a space
# Input: ['938-242-504']
# Output: (938) 242-504

def format_phone_number(input):
    input_str = input[0]
    first_three = input_str[:3]
    rest = input_str[4:]
    output = f"({first_three}) {rest}"
    return output

# Test the function with the given input
input = ['938-242-504']
output = format_phone_number(input)
print(output)  # Output should be (938) 242-504
