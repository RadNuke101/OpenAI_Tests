# Prompt: return the second input followed by a comma and a space, and then the first letter of the first input followed by a period
# Input: ['Launa', 'Withers'] 
# Output: Withers, L.

def format_names(inputs):
    first_name = inputs[0]
    last_name = inputs[1]
    
    output = last_name + ', ' + first_name[0] + '.'
    
    return output

# Test cases
print(format_names(['Launa', 'Withers']))  # Output: Withers, L.
print(format_names(['Lakenya', 'Edison']))  # Output: Edison, L.
print(format_names(['Brendan', 'Hage']))    # Output: Hage, B.
print(format_names(['Bradford', 'Lango']))  # Output: Lango, B.
print(format_names(['Rudolf', 'Akiyama']))  # Output: Akiyama, R.
Withers, L.
Edison, L.
Hage, B.
Lango, B.
Akiyama, R.
