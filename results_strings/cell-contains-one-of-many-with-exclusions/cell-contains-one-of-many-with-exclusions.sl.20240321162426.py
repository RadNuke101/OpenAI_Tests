# Prompt: if only one of the inputs from the second, third, or fourth column are in the first two words of the first input (first column), return true, else false
# Input: ['yellow dog on green grass', 'yellow', 'green', 'cat']
# Output: true

def check_inputs(input_str):
    input_list = input_str.split(', ')
    first_input = input_list[0].split()
    second_input = input_list[1]
    third_input = input_list[2]
    fourth_input = input_list[3]

    count = 0
    if second_input in first_input[:2]:
        count += 1
    if third_input in first_input[:2]:
        count += 1
    if fourth_input in first_input[:2]:
        count += 1

    return count == 1

# Test cases
print(check_inputs('yellow dog on green grass, yellow, green, cat'))  # Output: True
print(check_inputs('warm gray sweater, yellow, green, cat'))  # Output: False
print(check_inputs('blue neon signs, blue, green, neon'))  # Output: False
print(check_inputs('hot pink socks, blue, pink, neon'))  # Output: True
print(check_inputs('deep black eyes, yellow, green, neon'))  # Output: False
