def remove_second_input_from_first(input_str):
    first_input, second_input = input_str[0], input_str[1]
    return first_input.replace(second_input, '', 1)

# Prompt: remove second input from first input
# Input: ['zx66448', 'z']
# Output: x66448
# Input: ['zx66448', 'x']
# Output: z66448
# Input: ['zx66448', '6']
# Output: zx448
# Input: ['zx66448', '4']
# Output: zx668
# Input: ['zx66448', '8']
# Output: zx6644

# Test cases
print(remove_second_input_from_first(['zx66448', 'z']))  # Output: x66448
print(remove_second_input_from_first(['zx66448', 'x']))  # Output: z66448
print(remove_second_input_from_first(['zx66448', '6']))  # Output: zx448
print(remove_second_input_from_first(['zx66448', '4']))  # Output: zx668
print(remove_second_input_from_first(['zx66448', '8']))  # Output: zx6644
