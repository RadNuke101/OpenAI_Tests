# Prompt: return phrase containing three capitalized letters in the beginning
# Input: ['Tire Pressure ABC123873 Monitor']
# Output: ABC123873

def extract_capitalized_letters(input_str):
    words = input_str.split()
    for word in words:
        if word.isupper() and len(word) >= 3:
            return word

# Test cases
print(extract_capitalized_letters('Tire Pressure ABC123873 Monitor'))  # Output: ABC123873
print(extract_capitalized_letters('Oil Life ABC849999999021 gauge'))    # Output: ABC849999999021
print(extract_capitalized_letters('Air conditioner GHF211 maintenance'))  # Output: GHF211
