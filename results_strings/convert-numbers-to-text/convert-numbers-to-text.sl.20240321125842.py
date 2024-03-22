# Prompt: return the input, and given input as ['101'] output is 101, given input as ['1002'] output is 1002, given input as ['743'] output is 743

def return_input(input_str):
    return int(input_str[0])

# Test cases
print(return_input(['101']))  # Output: 101
print(return_input(['1002']))  # Output: 1002
print(return_input(['743']))  # Output: 743
