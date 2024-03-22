def first_letter_period(input_str):
    input_list = input_str.split(', ')
    first_letter = input_list[0][0]
    output = first_letter + '. ' + input_list[1]
    return output

# Prompt: return the first letter of the first input, followed by a period and a space, and then the second input
# Input: ['Launa', 'Withers']
# Output: L. Withers

# Test cases
print(first_letter_period('Launa, Withers'))  # L. Withers
print(first_letter_period('Lakenya, Edison'))  # L. Edison
print(first_letter_period('Brendan, Hage'))  # B. Hage
print(first_letter_period('Bradford, Lango'))  # B. Lango
print(first_letter_period('Rudolf, Akiyama'))  # R. Akiyama
print(first_letter_period('Lara, Constable'))  # L. Constable
