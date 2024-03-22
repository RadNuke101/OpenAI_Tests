def format_names(input):
    first_name = input[0]
    last_name = input[1]
    output = f"{first_name} {last_name[0]}."
    return output

# Prompt: return the first input, followed by a space, and then the the first letter of the second input, followed by a period
# Input: ['Nancy', 'FreeHafer']
# Output: Nancy F.

# Test cases
print(format_names(['Nancy', 'FreeHafer']))  # Output: Nancy F.
print(format_names(['Andrew', 'Cencici']))  # Output: Andrew C.
print(format_names(['Jan', 'Kotas']))  # Output: Jan K.
print(format_names(['Mariya', 'Sergienko']))  # Output: Mariya S.
print(format_names(['Launa', 'Withers']))  # Output: Launa W.
print(format_names(['Lakenya', 'Edison']))  # Output: Lakenya E.
