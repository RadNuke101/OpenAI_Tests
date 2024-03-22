# Prompt: return input with parentheses around the first three numbers and delete the first "-" and replace it with a space
# Input: ['938-242-504']
# Output: (938) 242-504

def format_phone_number(input):
    phone_number = input[0]
    area_code = phone_number[:3]
    rest_of_number = phone_number[4:]
    formatted_number = f"({area_code}) {rest_of_number}"
    return formatted_number

# Test the function with the given input
input = ['938-242-504']
output = format_phone_number(input)
print(output)  # Output should be (938) 242-504
