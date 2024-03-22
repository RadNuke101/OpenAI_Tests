# Prompt: return everything after the last '.' in the inputted expression
# Input: ['www.domain.com'], Output: com
# Input: ['mail.net'], Output: net
# Input: ['www.amaon.co.uk'], Output: uk

def get_last_domain(input_str):
    return input_str.split('.')[-1]

# Test cases
print(get_last_domain('www.domain.com'))  # Output: com
print(get_last_domain('mail.net'))        # Output: net
print(get_last_domain('www.amaon.co.uk')) # Output: uk
