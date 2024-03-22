# Prompt: return the phrase (space on at least one end) in the inputted expression that ends with ".com"
# Input: ['send email to json_acme.com']
# Output: json_acme.com

def find_com_phrase(input_str):
    words = input_str.split()
    for word in words:
        if word.endswith(".com"):
            return word.strip()

# Test cases
print(find_com_phrase('send email to json_acme.com'))  # Output: json_acme.com
print(find_com_phrase('contact help_robot.com for all support requests'))  # Output: help_robot.com
