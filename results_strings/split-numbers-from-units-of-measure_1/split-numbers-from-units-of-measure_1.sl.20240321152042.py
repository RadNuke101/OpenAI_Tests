# Prompt: return the numbers from first input
# Input: ['80v', '3'] 
# Output: 80

def extract_number(input):
    num = ''
    for char in input:
        if char.isdigit():
            num += char
        elif char == 'h' or char == 'm':
            break
    return int(num)

# Test cases
print(extract_number('80v'))  # Output: 80
print(extract_number('10hrs'))  # Output: 10
print(extract_number('7h'))  # Output: 7
print(extract_number('500m'))  # Output: 500
