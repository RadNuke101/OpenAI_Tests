# Prompt: return the second input followed by a comma and a space, and then the first letter of the first input followed by a period
# Input: ['Launa', 'Withers'] 
# Output: Withers, L.

def format_output(input_list):
    output = input_list[1] + ', ' + input_list[0][0] + '.'
    return output

# Test cases
print(format_output(['Launa', 'Withers']))  # Output: Withers, L.
print(format_output(['Lakenya', 'Edison']))  # Output: Edison, L.
print(format_output(['Brendan', 'Hage']))  # Output: Hage, B.
print(format_output(['Bradford', 'Lango']))  # Output: Lango, B.
print(format_output(['Rudolf', 'Akiyama']))  # Output: Akiyama, R.
