# Prompt: return the phrase (space on atleast one end) in the inputted expression that ends with ".com"
# Input: ['send email to json_acme.com']
# Output: json_acme.com

def find_phrase_with_com(input_str):
    words = input_str.split()
    for word in words:
        if word.endswith(".com"):
            return word.strip()

# Test the function with the given inputs
input1 = 'send email to json_acme.com'
output1 = find_phrase_with_com(input1)
print(output1)  # Output: json_acme.com

input2 = 'contact help_robot.com for all support requests'
output2 = find_phrase_with_com(input2)
print(output2)  # Output: help_robot.com
