def first_letter_period(input_str):
    # Prompt: return the first letter of the first input, followed by a period and a space, and then the second input
    # Input: ['Launa', 'Withers'] -> Output: L. Withers
    first_name, last_name = input_str.split(', ')
    return f"{first_name[0]}. {last_name}"

# Test cases
print(first_letter_period('Launa, Withers'))  # Output: L. Withers
print(first_letter_period('Lakenya, Edison'))  # Output: L. Edison
print(first_letter_period('Brendan, Hage'))  # Output: B. Hage
print(first_letter_period('Bradford, Lango'))  # Output: B. Lango
print(first_letter_period('Rudolf, Akiyama'))  # Output: R. Akiyama
print(first_letter_period('Lara, Constable'))  # Output: L. Constable
