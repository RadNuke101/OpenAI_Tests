# Prompt: return the numbers from first input
# Input: '80v', '3'
# Output: 80

def extract_number(input_str):
    num = ''
    for char in input_str:
        if char.isdigit():
            num += char
        else:
            break
    return int(num)

# Test cases
print(extract_number('80v'))  # Output: 80
print(extract_number('10hrs'))  # Output: 10
print(extract_number('7h'))  # Output: 7
print(extract_number('500m'))  # Output: 500
