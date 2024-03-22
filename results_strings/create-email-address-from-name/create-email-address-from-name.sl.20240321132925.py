# Prompt: take the first letter of the second input and add it to the front of the first input, then add "_acme.com" at the end
# Input: ['brown', 'traci'] Output: tbrown_acme.com
# Input: ['thomas', 'linda'] Output: lthomas_acme.com
# Input: ['ward', 'jack'] Output: jward_acme.com

def generate_email(input_list):
    first_input = input_list[0]
    second_input = input_list[1]
    
    new_input = second_input[0] + first_input
    output = new_input + '_acme.com'
    
    return output

# Test cases
print(generate_email(['brown', 'traci']))  # Output: tbrown_acme.com
print(generate_email(['thomas', 'linda']))  # Output: lthomas_acme.com
print(generate_email(['ward', 'jack']))  # Output: jward_acme.com
tbrown_acme.com
lthomas_acme.com
jward_acme.com
