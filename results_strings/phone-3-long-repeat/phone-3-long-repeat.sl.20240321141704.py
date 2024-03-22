# Prompt: return input with parentheses around the first three numbers and delete the first "-" and replace it with a space
# Input: ['938-242-504']
# Output: (938) 242-504

def format_phone_number(input):
    # Extract the numbers from the input string
    numbers = input[0].split('-')
    
    # Format the numbers according to the prompt
    formatted_number = f"({numbers[0]}) {numbers[1]}-{numbers[2]}"
    
    return formatted_number

# Test the function with the given input
input = ['938-242-504']
output = format_phone_number(input)
print(output)  # Output: (938) 242-504
