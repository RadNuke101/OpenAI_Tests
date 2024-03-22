def first_letter_period(input_str):
    input_list = input_str.split(', ')
    first_letter = input_list[0][0]
    output = first_letter + '. ' + input_list[1]
    return output

# Prompt: return the first letter of the first input, followed by a period and a space, and then the second input
# Input: ['Launa', 'Withers']
# Output: L. Withers
print(first_letter_period('Launa, Withers'))

# Input: ['Lakenya', 'Edison']
# Output: L. Edison
print(first_letter_period('Lakenya, Edison'))

# Input: ['Brendan', 'Hage']
# Output: B. Hage
print(first_letter_period('Brendan, Hage'))

# Input: ['Bradford', 'Lango']
# Output: B. Lango
print(first_letter_period('Bradford, Lango'))

# Input: ['Rudolf', 'Akiyama']
# Output: R. Akiyama
print(first_letter_period('Rudolf, Akiyama'))
