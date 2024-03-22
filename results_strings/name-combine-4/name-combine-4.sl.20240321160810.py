# Prompt: return the second input followed by a comma and a space, and then the first letter of the first input followed by a period
# Input: ['Launa', 'Withers'] 
# Output: Withers, L.

def format_output(inputs):
    return inputs[1] + ', ' + inputs[0][0] + '.'

# Test cases
print(format_output(['Launa', 'Withers']))  # Output: Withers, L.
print(format_output(['Lakenya', 'Edison']))  # Output: Edison, L.
print(format_output(['Brendan', 'Hage']))  # Output: Hage, B.
print(format_output(['Bradford', 'Lango']))  # Output: Lango, B.
print(format_output(['Rudolf', 'Akiyama']))  # Output: Akiyama, R.
Withers, L.
Edison, L.
Hage, B.
Lango, B.
Akiyama, R.
