def format_phone_number(input):
    input = input[0]
    output = input.replace("+", "").replace("-", ".").replace(" ", "")
    return output

# Prompt: return input, but remove the "+", add a "." in empty space, and replace all "-" with a "."
# Input: ['+45 095-746-635']
# Output: '45.095.746.635'

print(format_phone_number(['+45 095-746-635']))
