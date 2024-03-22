def first_letter_name(input_str):
    input_list = input_str.split(', ')
    first_name = input_list[0]
    last_name = input_list[1]
    return f"{first_name[0]}. {last_name}"

# Prompt: return the first letter of the first input, followed by a period and a space, and then the second input
# Input: 'Launa, Withers'
# Output: 'L. Withers'

# Test cases
print(first_letter_name('Launa, Withers'))  # Output: 'L. Withers'
print(first_letter_name('Lakenya, Edison'))  # Output: 'L. Edison'
print(first_letter_name('Brendan, Hage'))  # Output: 'B. Hage'
print(first_letter_name('Bradford, Lango'))  # Output: 'B. Lango'
print(first_letter_name('Rudolf, Akiyama'))  # Output: 'R. Akiyama'
print(first_letter_name('Lara, Constable'))  # Output: 'L. Constable'
