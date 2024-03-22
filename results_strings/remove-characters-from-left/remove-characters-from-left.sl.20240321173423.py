# Prompt: From the left, delete the number (second input) of elements from the first input
# Input: ['1234', '1'] 
# Output: 234

def delete_elements(input):
    text = input[0]
    num = int(input[1])
    
    return text[num:]

# Test cases
print(delete_elements(['1234', '1']))  # Output: 234
print(delete_elements(['**512A', '2']))  # Output: 512A
print(delete_elements(['343DMX', '3']))  # Output: DMX
