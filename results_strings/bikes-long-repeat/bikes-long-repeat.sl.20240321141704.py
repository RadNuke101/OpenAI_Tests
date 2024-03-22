def get_text_before_last_3_numbers(input_str):
    text = input_str[:-3]
    return text

# Prompt: return the text before the last 3 numbers in inputted expression
# Input: ['Ducati100'] 
# Output: Ducati

# Test cases
print(get_text_before_last_3_numbers('Ducati100'))  # Output: Ducati
print(get_text_before_last_3_numbers('Honda125'))  # Output: Honda
print(get_text_before_last_3_numbers('Ferrari250'))  # Output: Ferrari
print(get_text_before_last_3_numbers('Acura125'))  # Output: Acura
Ducati
Honda
Ferrari
Acura
