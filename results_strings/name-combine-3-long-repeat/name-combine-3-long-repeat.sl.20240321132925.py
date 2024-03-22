# Prompt: return the first letter of the first input, followed by a period and a space, and then the second input
# Input: ['Launa', 'Withers']
# Output: L. Withers

def first_letter_period_second(input_str):
    input_list = input_str.split(', ')
    first_letter = input_list[0][0]
    return first_letter + '. ' + input_list[1]

# Test the function with the given inputs
print(first_letter_period_second('Launa, Withers'))  # Output: L. Withers
print(first_letter_period_second('Lakenya, Edison'))  # Output: L. Edison
print(first_letter_period_second('Brendan, Hage'))  # Output: B. Hage
