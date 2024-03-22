# Prompt: return the text before the last 3 numbers in inputted expression
# Input: 'Ducati100', Output: 'Ducati'
# Input: 'Honda125', Output: 'Honda'
# Input: 'Ducati250', Output: 'Ducati'
# Input: 'Honda250', Output: 'Honda'
# Input: 'Honda550', Output: 'Honda'
# Input: 'Ducati125', Output: 'Ducati'
# Input: 'Acura100', Output: 'Acura'
# Input: 'Acura125', Output: 'Acura'
# Input: 'Ferrari250', Output: 'Ferrari'

def get_text_before_last_three_numbers(input_str):
    return input_str[:-3]

# Test cases
print(get_text_before_last_three_numbers('Ducati100'))  # Output: Ducati
print(get_text_before_last_three_numbers('Honda125'))  # Output: Honda
print(get_text_before_last_three_numbers('Ducati250'))  # Output: Ducati
print(get_text_before_last_three_numbers('Honda250'))  # Output: Honda
print(get_text_before_last_three_numbers('Honda550'))  # Output: Honda
print(get_text_before_last_three_numbers('Ducati125'))  # Output: Ducati
print(get_text_before_last_three_numbers('Acura100'))  # Output: Acura
print(get_text_before_last_three_numbers('Acura125'))  # Output: Acura
print(get_text_before_last_three_numbers('Ferrari250'))  # Output: Ferrari
