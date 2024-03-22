# Prompt: remove numbers from first input
# Input: ['80v', '3'] 
# Output: v

def remove_numbers(input):
    input_str = input[0]
    num_to_remove = int(input[1])
    
    output = ''.join([char for char in input_str if not char.isdigit()])
    
    return output

# Test cases
print(remove_numbers(['80v', '3']))  # Output: v
print(remove_numbers(['10hrs', '3']))  # Output: hrs
print(remove_numbers(['7h', '2']))  # Output: h
print(remove_numbers(['500m', '4']))  # Output: m
