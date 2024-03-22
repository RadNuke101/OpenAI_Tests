# Prompt: delete the last phrase / word if all the letters are capitalized
# Input: ['Mining US'] 
# Output: Mining

def process_input(input_str):
    words = input_str.split()
    if words[-1].isupper():
        return ' '.join(words[:-1])
    return input_str

# Test cases
print(process_input('Mining US')) # Output: Mining
print(process_input('Soybean Farming CAN')) # Output: Soybean Farming
print(process_input('Soybean Farming')) # Output: Soybean Farming
print(process_input('Oil Extraction US')) # Output: Oil Extraction
print(process_input('Fishing')) # Output: Fishing
