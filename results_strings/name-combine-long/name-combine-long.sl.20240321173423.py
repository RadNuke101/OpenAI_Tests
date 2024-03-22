# Prompt: return first input followed by a space, and then the second input
# Input: ['Launa', 'Withers'] 
# Output: Launa Withers

def combine_names(inputs):
    return inputs[0] + ' ' + inputs[1]

# Test cases
print(combine_names(['Launa', 'Withers'])) # Launa Withers
print(combine_names(['Lakenya', 'Edison'])) # Lakenya Edison
print(combine_names(['Brendan', 'Hage'])) # Brendan Hage
print(combine_names(['Bradford', 'Lango'])) # Bradford Lango
print(combine_names(['Rudolf', 'Akiyama'])) # Rudolf Akiyama
