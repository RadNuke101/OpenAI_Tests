# Prompt: take the first letter of the second input and add it to the front of the first input, then add "_acme.com" at the end
# Input: ['brown', 'traci'] Output: tbrown_acme.com
# Input: ['thomas', 'linda'] Output: lthomas_acme.com
# Input: ['ward', 'jack'] Output: jward_acme.com

def generate_email(input):
    first_word = input[0]
    second_word = input[1]
    
    new_word = second_word[0] + first_word + '_acme.com'
    
    return new_word

# Test the function with the given inputs
print(generate_email(['brown', 'traci']))  # Output: tbrown_acme.com
print(generate_email(['thomas', 'linda']))  # Output: lthomas_acme.com
print(generate_email(['ward', 'jack']))  # Output: jward_acme.com
