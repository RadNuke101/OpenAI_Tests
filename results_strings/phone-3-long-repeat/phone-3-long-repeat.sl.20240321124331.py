def format_phone_number(input):
    # Prompt: return input with parentheses around the first three numbers and delete the first "-" and replace it with a space
    # Input: ['938-242-504'], Output: (938) 242-504
    # Input: ['308-916-545'], Output: (308) 916-545
    # Input: ['623-599-749'], Output: (623) 599-749
    
    input_str = input[0]
    first_three = input_str[:3]
    rest = input_str[4:]
    
    return f"({first_three}) {rest}"

# Test the function with the provided inputs
print(format_phone_number(['938-242-504']))  # Output: (938) 242-504
print(format_phone_number(['308-916-545']))  # Output: (308) 916-545
print(format_phone_number(['623-599-749']))  # Output: (623) 599-749
