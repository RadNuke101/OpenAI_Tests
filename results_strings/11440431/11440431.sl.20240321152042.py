# Prompt: delete the last phrase / word if all the letters are capitalized
# Input: ['Mining US'] -> Output: Mining
# Input: ['Soybean Farming CAN'] -> Output: Soybean Farming
# Input: ['Soybean Farming'] -> Output: Soybean Farming
# Input: ['Oil Extraction US'] -> Output: Oil Extraction
# Input: ['Fishing'] -> Output: Fishing

def process_input(input_list):
    input_str = input_list[0]
    words = input_str.split()
    
    for i in range(len(words) - 1, -1, -1):
        if words[i].isupper():
            return ' '.join(words[:i])
    
    return input_str

# Test cases
print(process_input(['Mining US']))  # Output: Mining
print(process_input(['Soybean Farming CAN']))  # Output: Soybean Farming
print(process_input(['Soybean Farming']))  # Output: Soybean Farming
print(process_input(['Oil Extraction US']))  # Output: Oil Extraction
print(process_input(['Fishing']))  # Output: Fishing
