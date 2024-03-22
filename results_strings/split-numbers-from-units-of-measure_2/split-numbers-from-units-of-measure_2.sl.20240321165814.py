# Prompt: remove numbers from first input
# Input: ['80v', '3'] 
# Output: v

def remove_numbers(input):
    first_input = input[0]
    second_input = input[1]
    
    output = ''.join([char for char in first_input if not char.isdigit()])
    
    return output

# Test cases
print(remove_numbers(['80v', '3']))  # Output: v
print(remove_numbers(['10hrs', '3']))  # Output: hrs
print(remove_numbers(['7h', '2']))  # Output: h
print(remove_numbers(['500m', '4']))  # Output: m
