def format_phone_number(input_str):
    # Prompt: return input with parentheses around the first three numbers and delete the first "-" and replace it with a space
    input_str = input_str.replace("-", " ", 1)
    output_str = "(" + input_str[:3] + ") " + input_str[4:]
    return output_str

# Test cases
print(format_phone_number('938-242-504'))  # Output: (938) 242-504
print(format_phone_number('308-916-545'))  # Output: (308) 916-545
print(format_phone_number('623-599-749'))  # Output: (623) 599-749
