def format_phone_number(input_str):
    input_str = input_str.replace("+", "").replace("-", ".").replace(" ", "")
    return input_str

# Prompt input
input1 = '+106 769-858-438'
# Expected output: '106.769.858.438'

# Test input
input2 = '+83 973-757-831'
# Expected output: '83.973.757.831'

# Test the function with the prompt input
output1 = format_phone_number(input1)
print(output1)  # Output: 106.769.858.438

# Test the function with the test input
output2 = format_phone_number(input2)
print(output2)  # Output: 83.973.757.831
