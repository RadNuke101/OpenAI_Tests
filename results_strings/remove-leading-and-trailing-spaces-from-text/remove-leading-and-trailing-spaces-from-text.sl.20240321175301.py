# Prompt: remove spaces from the beginning and end of input
# Input: ['  The shawshank']
# Output: The shawshank

def remove_spaces(input_str):
    output_str = input_str.strip()
    return output_str

# Test cases
print(remove_spaces('  The shawshank'))  # Output: The shawshank
print(remove_spaces('The    godfather'))  # Output: The godfather
print(remove_spaces('    pulp   fiction'))  # Output: pulp fiction
