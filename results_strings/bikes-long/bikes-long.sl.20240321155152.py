def get_text_before_last_3_numbers(input_str):
    text = input_str[:-3]
    return text

# Prompt: return the text before the last 3 numbers in inputted expression
# Input: 'Ducati100'
# Output: 'Ducati'
print(get_text_before_last_3_numbers('Ducati100'))  # Ducati

# Input: 'Honda125'
# Output: 'Honda'
print(get_text_before_last_3_numbers('Honda125'))  # Honda

# Input: 'Ducati250'
# Output: 'Ducati'
print(get_text_before_last_3_numbers('Ducati250'))  # Ducati

# Input: 'Honda250'
# Output: 'Honda'
print(get_text_before_last_3_numbers('Honda250'))  # Honda

# Input: 'Honda550'
# Output: 'Honda'
print(get_text_before_last_3_numbers('Honda550'))  # Honda

# Input: 'Ducati125'
# Output: 'Ducati'
print(get_text_before_last_3_numbers('Ducati125'))  # Ducati

# Input: 'Acura100'
# Output: 'Acura'
print(get_text_before_last_3_numbers('Acura100'))  # Acura

# Input: 'Acura125'
# Output: 'Acura'
print(get_text_before_last_3_numbers('Acura125'))  # Acura

# Input: 'Ferrari250'
# Output: 'Ferrari'
print(get_text_before_last_3_numbers('Ferrari250'))  # Ferrari
