# Prompt: return the three numbers between the "-", 
# Input: ['938-242-504'] Output: 242
# Input: ['308-916-545'] Output: 916
# Input: ['623-599-749'] Output: 599
# Input: ['981-424-843'] Output: 424
# Input: ['118-980-214'] Output: 980
# Input: ['244-655-094'] Output: 655

def extract_number(input_str):
    numbers = input_str.split('-')
    return numbers[1]

# Test cases
print(extract_number('938-242-504'))  # Output: 242
print(extract_number('308-916-545'))  # Output: 916
print(extract_number('623-599-749'))  # Output: 599
print(extract_number('981-424-843'))  # Output: 424
print(extract_number('118-980-214'))  # Output: 980
print(extract_number('244-655-094'))  # Output: 655
242
916
599
424
980
655
