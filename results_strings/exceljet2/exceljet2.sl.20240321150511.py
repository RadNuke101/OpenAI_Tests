# Prompt: return everything after the last '.' in the inputted expression
# Input: ['www.domain.com'], Output: com
# Input: ['mail.net'], Output: net
# Input: ['www.amaon.co.uk'], Output: uk

def get_last_segment(input_str):
    segments = input_str.split('.')
    return segments[-1]

# Test cases
print(get_last_segment('www.domain.com'))  # Output: com
print(get_last_segment('mail.net'))  # Output: net
print(get_last_segment('www.amaon.co.uk'))  # Output: uk
