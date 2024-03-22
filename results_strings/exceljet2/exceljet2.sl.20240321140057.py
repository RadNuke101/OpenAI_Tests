# Prompt: return everything after the last '.' in the inputted expression
# Input: ['www.domain.com'] 
# Output: com
def get_domain(input_str):
    return input_str.split('.')[-1]

# Test cases
print(get_domain('www.domain.com'))  # Output: com
print(get_domain('mail.net'))  # Output: net
print(get_domain('www.amazon.co.uk'))  # Output: uk
