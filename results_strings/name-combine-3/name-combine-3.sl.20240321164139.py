# Prompt: return the first letter of the first input, followed by a period and a space, and then the second input
# Input: ['Launa', 'Withers']
# Output: L. Withers

def format_output(inputs):
    return f"{inputs[0][0]}. {inputs[1]}"

# Test cases
print(format_output(['Launa', 'Withers']))  # Output: L. Withers
print(format_output(['Lakenya', 'Edison']))  # Output: L. Edison
print(format_output(['Brendan', 'Hage']))  # Output: B. Hage
print(format_output(['Bradford', 'Lango']))  # Output: B. Lango
print(format_output(['Rudolf', 'Akiyama']))  # Output: R. Akiyama
print(format_output(['Lara', 'Constable']))  # Output: L. Constable
