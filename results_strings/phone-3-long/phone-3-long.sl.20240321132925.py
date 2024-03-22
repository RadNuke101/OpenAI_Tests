def format_phone_number(input_str):
    # Prompt: return input with parentheses around the first three numbers and delete the first "-" and replace it with a space
    # Input: ['938-242-504'] -> Output: (938) 242-504
    
    # Extract the numbers from the input string
    numbers = input_str.split('-')
    
    # Format the numbers according to the prompt
    output = f"({numbers[0]}) {numbers[1]}-{numbers[2]}"
    
    return output

# Test cases
print(format_phone_number('938-242-504'))  # Output: (938) 242-504
print(format_phone_number('308-916-545'))  # Output: (308) 916-545
print(format_phone_number('623-599-749'))  # Output: (623) 599-749
print(format_phone_number('981-424-843'))  # Output: (981) 424-843
print(format_phone_number('118-980-214'))  # Output: (118) 980-214
