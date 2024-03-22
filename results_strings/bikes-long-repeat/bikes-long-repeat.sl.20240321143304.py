def get_text_before_last_three_numbers(input_str):
    text = input_str[:-3]
    return text

# Prompt: return the text before the last 3 numbers in inputted expression
# Input: ['Ducati100'] 
# Output: Ducati

# Test cases
print(get_text_before_last_three_numbers('Ducati100'))  # Output: Ducati
print(get_text_before_last_three_numbers('Honda125'))  # Output: Honda
print(get_text_before_last_three_numbers('Ferrari250'))  # Output: Ferrari
print(get_text_before_last_three_numbers('Acura100'))  # Output: Acura
Ducati
Honda
Ferrari
Acura
