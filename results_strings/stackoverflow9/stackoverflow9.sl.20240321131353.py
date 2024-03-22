# Prompt: return last word/phrase from input
# Input: ['Sarah Jane Jones']
# Output: Jones

def return_last_word(input_str):
    words = input_str.split()
    return words[-1]

# Test cases
input1 = 'Sarah Jane Jones'
input2 = 'Bob Jane Smithfield'

output1 = return_last_word(input1)
output2 = return_last_word(input2)

print(output1)  # Jones
print(output2)  # Smithfield
