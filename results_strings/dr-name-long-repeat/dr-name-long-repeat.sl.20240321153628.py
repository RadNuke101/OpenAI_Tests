def add_title(input_str):
    # Prompt: return "Dr. " and the first input after
    return "Dr. " + input_str.split()[0]

# Input: 'Launa Withers'
# Output: 'Dr. Launa'
print(add_title('Launa Withers'))

# Input: 'Lakenya Edison'
# Output: 'Dr. Lakenya'
print(add_title('Lakenya Edison'))

# Input: 'Brendan Hage'
# Output: 'Dr. Brendan'
print(add_title('Brendan Hage'))

# Continue testing with other inputs...
