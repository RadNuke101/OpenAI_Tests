# Prompt: take the first letter of the second input and add it to the front of the first input, then add "_acme.com" at the end
# Input: ['brown', 'traci'] Output: tbrown_acme.com
# Input: ['thomas', 'linda'] Output: lthomas_acme.com
# Input: ['ward', 'jack'] Output: jward_acme.com

def generate_email(input1, input2):
    output = input2[0] + input1 + "_acme.com"
    return output

# Test cases
print(generate_email('brown', 'traci'))  # Output: tbrown_acme.com
print(generate_email('thomas', 'linda'))  # Output: lthomas_acme.com
print(generate_email('ward', 'jack'))  # Output: jward_acme.com
tbrown_acme.com
lthomas_acme.com
jward_acme.com
