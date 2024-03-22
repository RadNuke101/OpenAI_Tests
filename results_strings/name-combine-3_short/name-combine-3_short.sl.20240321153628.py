def first_letter_period(input):
    first_name = input.split()[0]
    first_letter = first_name[0]
    last_name = input.split()[1]
    return f"{first_letter}. {last_name}"

# Input: 'Launa Withers'
# Output: 'L. Withers'
# Prompt: return the first letter of the first input, followed by a period and a space, and then the second input
print(first_letter_period('Launa Withers'))  # Output: L. Withers

print(first_letter_period('Lakenya Edison'))  # Output: L. Edison
print(first_letter_period('Brendan Hage'))  # Output: B. Hage
print(first_letter_period('Bradford Lango'))  # Output: B. Lango
print(first_letter_period('Rudolf Akiyama'))  # Output: R. Akiyama
print(first_letter_period('Lara Constable'))  # Output: L. Constable
