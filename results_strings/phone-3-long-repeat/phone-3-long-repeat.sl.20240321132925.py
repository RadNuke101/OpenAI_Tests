def format_phone_number(input):
    # Prompt: return input with parentheses around the first three numbers and delete the first "-" and replace it with a space
    # Given input as ['938-242-504'] output is (938) 242-504
    
    # Extract the phone number from the list input
    phone_number = input[0]
    
    # Format the phone number as required
    formatted_number = "(" + phone_number[:3] + ") " + phone_number[4:]
    
    return formatted_number

# Test cases
print(format_phone_number(['938-242-504']))  # Output: (938) 242-504
print(format_phone_number(['308-916-545']))  # Output: (308) 916-545
print(format_phone_number(['623-599-749']))  # Output: (623) 599-749
print(format_phone_number(['981-424-843']))  # Output: (981) 424-843
print(format_phone_number(['118-980-214']))  # Output: (118) 980-214
print(format_phone_number(['244-655-094']))  # Output: (244) 655-094
