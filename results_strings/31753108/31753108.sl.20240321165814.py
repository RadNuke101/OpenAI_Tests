# Prompt: return phrase containing three capitalized letters in the beginning
# Input: ['Tire Pressure ABC123873 Monitor']
# Output: ABC123873

def extract_capitalized_letters(input_str):
    words = input_str.split()
    for word in words:
        if word.isupper() and len(word) >= 3:
            return word

# Test cases
input1 = 'Tire Pressure ABC123873 Monitor'
input2 = 'Oil Life ABC849999999021 gauge'
input3 = 'Air conditioner GHF211 maintenance'

output1 = extract_capitalized_letters(input1)
output2 = extract_capitalized_letters(input2)
output3 = extract_capitalized_letters(input3)

print(output1)  # ABC123873
print(output2)  # ABC849999999021
print(output3)  # GHF211
