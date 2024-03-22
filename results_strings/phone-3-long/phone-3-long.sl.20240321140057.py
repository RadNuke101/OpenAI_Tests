def format_phone_number(input_str):
    input_str = input_str[0]
    output = "(" + input_str[:3] + ") " + input_str[4:]
    return output

# Prompt: return input with parentheses around the first three numbers and delete the first "-" and replace it with a space
# Input: ['938-242-504'] 
# Output: (938) 242-504

print(format_phone_number(['938-242-504']))
