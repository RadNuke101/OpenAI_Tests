# Prompt: return the phrase (space on atleast one end) in the inputted expression that ends with ".com"
# Input: ['send email to json_acme.com']
# Output: json_acme.com

def find_com_phrase(input_str):
    words = input_str.split()
    for word in words:
        if word.endswith(".com"):
            return word.strip()

# Test cases
input1 = 'send email to json_acme.com'
input2 = 'contact help_robot.com for all support requests'

output1 = find_com_phrase(input1)
output2 = find_com_phrase(input2)

print(output1)  # json_acme.com
print(output2)  # help_robot.com
