# Prompt: return everything after the last '.' in the inputted expression
# Input: ['www.domain.com']  Output: com
# Input: ['mail.net']  Output: net
# Input: ['www.amaon.co.uk']  Output: uk

def get_last_part(input_str):
    parts = input_str.split('.')
    return parts[-1]

# Test cases
print(get_last_part('www.domain.com'))  # Output: com
print(get_last_part('mail.net'))  # Output: net
print(get_last_part('www.amaon.co.uk'))  # Output: uk
