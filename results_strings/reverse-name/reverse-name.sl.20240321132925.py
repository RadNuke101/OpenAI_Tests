# Prompt: return second input, followed by a space, and then the first input
# Input: ['Launa', 'Withers'] Output: Withers Launa
# Input: ['Lakenya', 'Edison'] Output: Edison Lakenya
# Input: ['Brendan', 'Hage'] Output: Hage Brendan
# Input: ['Bradford', 'Lango'] Output: Lango Bradford
# Input: ['Rudolf', 'Akiyama'] Output: Akiyama Rudolf
# Input: ['Lara', 'Constable'] Output: Constable Lara

def reverse_names(inputs):
    return inputs[1] + ' ' + inputs[0]

# Test cases
print(reverse_names(['Launa', 'Withers']))  # Output: Withers Launa
print(reverse_names(['Lakenya', 'Edison']))  # Output: Edison Lakenya
print(reverse_names(['Brendan', 'Hage']))  # Output: Hage Brendan
print(reverse_names(['Bradford', 'Lango']))  # Output: Lango Bradford
print(reverse_names(['Rudolf', 'Akiyama']))  # Output: Akiyama Rudolf
print(reverse_names(['Lara', 'Constable']))  # Output: Constable Lara
