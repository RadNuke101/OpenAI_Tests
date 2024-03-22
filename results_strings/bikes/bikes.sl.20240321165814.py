# Prompt: return the text before the last 3 numbers in inputted expression
# Input: ['Ducati100'], Output: Ducati
# Input: ['Honda125'], Output: Honda
# Input: ['Ducati250'], Output: Ducati
# Input: ['Honda250'], Output: Honda
# Input: ['Honda550'], Output: Honda
# Input: ['Ducati125'], Output: Ducati

def extract_text(input_str):
    return input_str[0:-3]

# Test cases
print(extract_text('Ducati100'))  # Output: Ducati
print(extract_text('Honda125'))   # Output: Honda
print(extract_text('Ducati250'))  # Output: Ducati
print(extract_text('Honda250'))   # Output: Honda
print(extract_text('Honda550'))   # Output: Honda
print(extract_text('Ducati125'))  # Output: Ducati
Ducati
Honda
Ducati
Honda
Honda
Ducati
