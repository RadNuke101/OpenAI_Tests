def get_text_before_last_3_numbers(input_str):
    text = input_str[:-3]
    return text

# Prompt: return the text before the last 3 numbers in inputted expression
# Input: 'Ducati100'
# Output: 'Ducati'
print(get_text_before_last_3_numbers('Ducati100'))  # Ducati

# Additional test cases
print(get_text_before_last_3_numbers('Honda125'))  # Honda
print(get_text_before_last_3_numbers('Ducati250'))  # Ducati
print(get_text_before_last_3_numbers('Honda250'))  # Honda
print(get_text_before_last_3_numbers('Honda550'))  # Honda
print(get_text_before_last_3_numbers('Ducati125'))  # Ducati
print(get_text_before_last_3_numbers('Acura100'))  # Acura
print(get_text_before_last_3_numbers('Acura125'))  # Acura
print(get_text_before_last_3_numbers('Ferrari250'))  # Ferrari
print(get_text_before_last_3_numbers('Ferrari250'))  # Ferrari
print(get_text_before_last_3_numbers('Honda550'))  # Honda
print(get_text_before_last_3_numbers('Ducati125'))  # Ducati
