def combine_names(input):
    return input[0] + ' ' + input[1]

# Prompt: return first input followed by a space, and then the second input
# Input: ['Launa', 'Withers'] 
# Output: 'Launa Withers'

# Test cases
print(combine_names(['Launa', 'Withers']))  # Output: 'Launa Withers'
print(combine_names(['Lakenya', 'Edison']))  # Output: 'Lakenya Edison'
print(combine_names(['Brendan', 'Hage']))  # Output: 'Brendan Hage'
print(combine_names(['Bradford', 'Lango']))  # Output: 'Bradford Lango'
print(combine_names(['Rudolf', 'Akiyama']))  # Output: 'Rudolf Akiyama'
print(combine_names(['Lara', 'Constable']))  # Output: 'Lara Constable'
