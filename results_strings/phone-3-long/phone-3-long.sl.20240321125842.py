def format_phone_number(input):
    input = input[0]
    output = "(" + input[:3] + ") " + input[4:]
    return output

# Prompt: return input with parentheses around the first three numbers and delete the first "-" and replace it with a space
# Input: ['938-242-504']
# Output: (938) 242-504

print(format_phone_number(['938-242-504']))
