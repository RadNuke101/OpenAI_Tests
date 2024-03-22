# Prompt: return the first letter of the first input, followed by a period and a space, and then the second input
# Given input as ['Launa', 'Withers'] output is L. Withers

def first_letter_period_second(input):
    return input[0][0] + ". " + input[1]

# Test cases
print(first_letter_period_second(['Launa', 'Withers']))  # Output: L. Withers
print(first_letter_period_second(['Lakenya', 'Edison']))  # Output: L. Edison
print(first_letter_period_second(['Brendan', 'Hage']))  # Output: B. Hage
print(first_letter_period_second(['Bradford', 'Lango']))  # Output: B. Lango
print(first_letter_period_second(['Rudolf', 'Akiyama']))  # Output: R. Akiyama
