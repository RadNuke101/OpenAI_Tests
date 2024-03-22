# Prompt: return input with parentheses around the first three numbers and delete the first "-" and replace it with a space
# Input: ['938-242-504'] => Output: (938) 242-504

def format_phone_number(phone_number):
    phone_number = phone_number[0]  # Extract the phone number from the list
    area_code = phone_number[:3]
    rest_of_number = phone_number[4:]
    formatted_number = f"({area_code}) {rest_of_number}"
    return formatted_number

# Test cases
print(format_phone_number(['938-242-504']))  # Output: (938) 242-504
print(format_phone_number(['308-916-545']))  # Output: (308) 916-545
print(format_phone_number(['623-599-749']))  # Output: (623) 599-749
print(format_phone_number(['981-424-843']))  # Output: (981) 424-843
print(format_phone_number(['118-980-214']))  # Output: (118) 980-214
print(format_phone_number(['244-655-094']))  # Output: (244) 655-094
