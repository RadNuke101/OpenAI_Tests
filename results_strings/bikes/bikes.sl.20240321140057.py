# Prompt: return the text before the last 3 numbers in inputted expression
# Input: ['Ducati100']  Output: Ducati
# Input: ['Honda125']  Output: Honda
# Input: ['Ducati250']  Output: Ducati
# Input: ['Honda250']  Output: Honda
# Input: ['Honda550']  Output: Honda
# Input: ['Ducati125']  Output: Ducati

def get_text_before_last_3_numbers(input_str):
    text = input_str[:-3]
    return text

# Test cases
print(get_text_before_last_3_numbers('Ducati100'))  # Output: Ducati
print(get_text_before_last_3_numbers('Honda125'))  # Output: Honda
print(get_text_before_last_3_numbers('Ducati250'))  # Output: Ducati
print(get_text_before_last_3_numbers('Honda250'))  # Output: Honda
print(get_text_before_last_3_numbers('Honda550'))  # Output: Honda
print(get_text_before_last_3_numbers('Ducati125'))  # Output: Ducati
Ducati
Honda
Ducati
Honda
Honda
Ducati
