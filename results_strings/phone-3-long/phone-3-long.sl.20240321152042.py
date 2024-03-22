def format_phone_number(input_str):
    input_str = input_str[0]
    output = "(" + input_str[:3] + ") " + input_str[4:]
    return output

# Prompt: return input with parentheses around the first three numbers and delete the first "-" and replace it with a space
# Input: ['938-242-504']
# Output: (938) 242-504

# Test cases
print(format_phone_number(['938-242-504']))  # (938) 242-504
print(format_phone_number(['308-916-545']))  # (308) 916-545
print(format_phone_number(['623-599-749']))  # (623) 599-749
print(format_phone_number(['981-424-843']))  # (981) 424-843
print(format_phone_number(['118-980-214']))  # (118) 980-214
print(format_phone_number(['244-655-094']))  # (244) 655-094
(938) 242-504
(308) 916-545
(623) 599-749
(981) 424-843
(118) 980-214
(244) 655-094
