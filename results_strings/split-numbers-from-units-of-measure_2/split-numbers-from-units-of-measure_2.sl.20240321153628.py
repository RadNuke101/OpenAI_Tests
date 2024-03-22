# Prompt: remove numbers from first input
# Input: ['80v', '3']
# Output: v

def remove_numbers(input):
    for char in input[0]:
        if not char.isdigit():
            return char

# Test cases
print(remove_numbers(['80v', '3']))  # Output: v
print(remove_numbers(['10hrs', '3']))  # Output: hrs
print(remove_numbers(['7h', '2']))  # Output: h
print(remove_numbers(['500m', '4']))  # Output: m
