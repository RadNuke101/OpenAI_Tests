# Prompt: return the first input, followed by a space, and then the second input
# Input: ['susan', 'chang']
# Output: susan chang

def combine_names(inputs):
    return ' '.join(inputs)

# Test cases
print(combine_names(['susan', 'chang']))  # Output: susan chang
print(combine_names(['aaron', 'kim']))  # Output: aaron kim
