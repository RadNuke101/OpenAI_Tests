# Prompt: return everything after the last '.' in the inputted expression
# Input: ['www.domain.com'], Output: com
# Input: ['mail.net'], Output: net
# Input: ['www.amaon.co.uk'], Output: uk

def get_last_extension(input_str):
    return input_str.split('.')[-1]

# Test cases
print(get_last_extension('www.domain.com'))  # Output: com
print(get_last_extension('mail.net'))  # Output: net
print(get_last_extension('www.amaon.co.uk'))  # Output: uk
