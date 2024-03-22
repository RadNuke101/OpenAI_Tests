def format_phone_number(input_str):
    # Prompt: return input with parentheses around the first three numbers before the first "-", delete the first "-" and replace it with a space
    # Input: ['+45 095-746-635']
    # Output: +45 (095) 746-635
    parts = input_str.split("-")
    first_part = parts[0]
    first_three_digits = "(" + first_part[-3:] + ")"
    new_input = first_part[:-3] + first_three_digits + " " + parts[1] + "-" + parts[2]
    return new_input

# Test the function with the provided input
input_str = '+45 095-746-635'
output_str = format_phone_number(input_str)
print(output_str)  # Output: +45 (095) 746-635
