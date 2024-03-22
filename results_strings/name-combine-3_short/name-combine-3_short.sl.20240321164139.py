# Prompt: return the first letter of the first input, followed by a period and a space, and then the second input
# Input: ['Launa', 'Withers'], Output: L. Withers
def first_letter_period_second(input):
    first_name = input[0]
    first_letter = first_name[0]
    output = first_letter + ". " + input[1]
    return output

# Test cases
print(first_letter_period_second(['Launa', 'Withers']))  # Output: L. Withers
print(first_letter_period_second(['Lakenya', 'Edison']))  # Output: L. Edison
print(first_letter_period_second(['Brendan', 'Hage']))  # Output: B. Hage
print(first_letter_period_second(['Bradford', 'Lango']))  # Output: B. Lango
print(first_letter_period_second(['Rudolf', 'Akiyama']))  # Output: R. Akiyama
print(first_letter_period_second(['Lara', 'Constable']))  # Output: L. Constable
