# Prompt: delete all "-", "<", ">", ".", and any spaces
# Input: ['801-456-8765']
# Output: 8014568765

def clean_phone_number(phone_number):
    cleaned_number = phone_number.replace("-", "").replace("<", "").replace(">", "").replace(".", "").replace(" ", "")
    return cleaned_number

# Test cases
print(clean_phone_number('801-456-8765'))  # Output: 8014568765
print(clean_phone_number('<978> 654-0299'))  # Output: 9786540299
print(clean_phone_number('978.654.0299'))  # Output: 9786540299
