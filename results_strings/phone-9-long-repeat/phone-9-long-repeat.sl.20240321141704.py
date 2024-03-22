# Prompt: return input, but remove the "+", add a "." in empty space, and replace all "-" with a "."
# Input: '+45 095-746-635'
# Output: '45.095.746.635'

def format_phone_number(input):
    input = input.replace("+", "").replace(" ", ".").replace("-", ".")
    return input

# Test the function with the given inputs
print(format_phone_number('+45 095-746-635'))  # Output: '45.095.746.635'
print(format_phone_number('+115 101-728-328'))  # Output: '115.101.728.328'
print(format_phone_number('+33 547-051-264'))  # Output: '33.547.051.264'
