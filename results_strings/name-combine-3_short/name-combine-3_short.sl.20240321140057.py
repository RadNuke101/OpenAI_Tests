# Prompt: return the first letter of the first input, followed by a period and a space, and then the second input
# Input: ['Launa', 'Withers']
# Output: L. Withers

def first_letter_and_last_name(inputs):
    first_letter = inputs[0][0]
    output = first_letter + ". " + inputs[1]
    return output

# Test cases
print(first_letter_and_last_name(['Launa', 'Withers']))  # Output: L. Withers
print(first_letter_and_last_name(['Lakenya', 'Edison']))  # Output: L. Edison
print(first_letter_and_last_name(['Brendan', 'Hage']))  # Output: B. Hage
print(first_letter_and_last_name(['Bradford', 'Lango']))  # Output: B. Lango
print(first_letter_and_last_name(['Rudolf', 'Akiyama']))  # Output: R. Akiyama
print(first_letter_and_last_name(['Lara', 'Constable']))  # Output: L. Constable
