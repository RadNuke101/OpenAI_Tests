# Prompt: return input with parentheses around the first three numbers and delete the first "-" and replace it with a space
# Input: ['938-242-504'] => Output: (938) 242-504

def format_phone_number(input_str):
    input_str = input_str[0]  # Extract the string from the list
    first_three = input_str[:3]
    rest = input_str[4:]
    output_str = f"({first_three}) {rest}"
    return output_str

# Test cases
print(format_phone_number(['938-242-504']))  # Output: (938) 242-504
print(format_phone_number(['308-916-545']))  # Output: (308) 916-545
print(format_phone_number(['623-599-749']))  # Output: (623) 599-749
print(format_phone_number(['981-424-843']))  # Output: (981) 424-843
print(format_phone_number(['118-980-214']))  # Output: (118) 980-214
print(format_phone_number(['244-655-094']))  # Output: (244) 655-094
