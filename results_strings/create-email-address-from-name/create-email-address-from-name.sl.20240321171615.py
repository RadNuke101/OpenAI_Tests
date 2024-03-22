# Prompt: take the first letter of the second input and add it to the front of the first input, then add "_acme.com" at the end
# Input: ['brown', 'traci'] Output: tbrown_acme.com
# Input: ['thomas', 'linda'] Output: lthomas_acme.com
# Input: ['ward', 'jack'] Output: jward_acme.com

def generate_email(input):
    first_letter = input[1][0]
    result = first_letter + input[0] + "_acme.com"
    return result

# Test cases
print(generate_email(['brown', 'traci']))  # Output: tbrown_acme.com
print(generate_email(['thomas', 'linda']))  # Output: lthomas_acme.com
print(generate_email(['ward', 'jack']))  # Output: jward_acme.com
tbrown_acme.com
lthomas_acme.com
jward_acme.com
