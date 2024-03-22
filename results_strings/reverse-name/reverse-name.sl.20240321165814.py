# Prompt: return second input, followed by a space, and then the first input
# Input: ['Launa', 'Withers']
# Output: Withers Launa

def rearrange_names(inputs):
    return inputs[1] + " " + inputs[0]

# Test cases
print(rearrange_names(['Launa', 'Withers']))  # Output: Withers Launa
print(rearrange_names(['Lakenya', 'Edison']))  # Output: Edison Lakenya
print(rearrange_names(['Brendan', 'Hage']))  # Output: Hage Brendan
print(rearrange_names(['Bradford', 'Lango']))  # Output: Lango Bradford
print(rearrange_names(['Rudolf', 'Akiyama']))  # Output: Akiyama Rudolf
print(rearrange_names(['Lara', 'Constable']))  # Output: Constable Lara
Withers Launa
Edison Lakenya
Hage Brendan
Lango Bradford
Akiyama Rudolf
Constable Lara
