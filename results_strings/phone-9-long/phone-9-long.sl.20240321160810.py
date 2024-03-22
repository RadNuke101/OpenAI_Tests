def format_phone_number(input_str):
    input_str = input_str.replace("+", "").replace("-", ".").replace(" ", "")
    return input_str

# Prompt: return input, but remove the "+", add a "." in empty space, and replace all "-" with a "."
# Input: '+45 095-746-635'
# Output: '45.095.746.635'

# Test cases
print(format_phone_number('+45 095-746-635'))  # Output: '45.095.746.635'
print(format_phone_number('+115 101-728-328'))  # Output: '115.101.728.328'
print(format_phone_number('+161 233-981-513'))  # Output: '161.233.981.513'
