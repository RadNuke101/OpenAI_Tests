# Prompt: return the phrase (space on atleast one end) in the inputted expression that ends with ".com"
# Input: ['send email to json_acme.com']
# Output: json_acme.com

def find_phrase_with_com(input_str):
    words = input_str.split()
    for word in words:
        if word.endswith(".com"):
            return word.strip()

# Test cases
print(find_phrase_with_com('send email to json_acme.com'))  # Output: json_acme.com
print(find_phrase_with_com('contact help_robot.com for all support requests'))  # Output: help_robot.com
