# Prompt: remove second input from first input
# Input: ['zx66448', 'z']
# Output: x66448

def remove_second_input(input_str, char):
    return input_str.replace(char, '', 1)

# Test cases
print(remove_second_input('zx66448', 'z')) # Output: x66448
print(remove_second_input('zx66448', 'x')) # Output: z66448
print(remove_second_input('zx66448', '6')) # Output: zx448
print(remove_second_input('zx66448', '4')) # Output: zx668
print(remove_second_input('zx66448', '8')) # Output: zx6644
