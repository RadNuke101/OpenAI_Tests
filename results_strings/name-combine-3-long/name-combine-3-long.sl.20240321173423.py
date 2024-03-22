def first_letter_period(input_str):
    input_list = input_str.split(', ')
    first_letter = input_list[0][0]
    output = first_letter + '. ' + input_list[1]
    return output

# Prompt: return the first letter of the first input, followed by a period and a space, and then the second input
# Given input as ['Launa', 'Withers'] output is L. Withers
# Given input as ['Lakenya', 'Edison'] output is L. Edison
# Given input as ['Brendan', 'Hage'] output is B. Hage

# Test cases
print(first_letter_period('Launa, Withers')) # Output: L. Withers
print(first_letter_period('Lakenya, Edison')) # Output: L. Edison
print(first_letter_period('Brendan, Hage')) # Output: B. Hage
