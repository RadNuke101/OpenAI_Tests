# Start time: 2024-03-30 02:33:20.123408
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: take the first letter of the second input and add it to the front of the first input, then add "_acme.com" at the end , and given input as ['brown', 'traci'] output is tbrown_acme.com, given input as ['thomas', 'linda'] output is lthomas_acme.com, given input as ['ward', 'jack'] output is jward_acme.com, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: take the first letter of the second input and add it to the front of the first input, then add "_acme.com" at the end
# Input: ['brown', 'traci'] Output: tbrown_acme.com
# Input: ['thomas', 'linda'] Output: lthomas_acme.com
# Input: ['ward', 'jack'] Output: jward_acme.com

def generate_email(input_list):
    try:
        if len(input_list) != 2:
            raise ValueError("Input list must contain exactly two elements")
        
        first_input = input_list[0]
        second_input = input_list[1]
        
        if not isinstance(first_input, str) or not isinstance(second_input, str):
            raise ValueError("Both inputs must be strings")
        
        if len(second_input) == 0:
            raise ValueError("Second input must not be an empty string")
        
        email = second_input[0] + first_input + "_acme.com"
        return email
    except ValueError as ve:
        return str(ve)

# Test cases
print(generate_email(['brown', 'traci']))  # Output: tbrown_acme.com
print(generate_email(['thomas', 'linda']))  # Output: lthomas_acme.com
print(generate_email(['ward', 'jack']))  # Output: jward_acme.com
print(generate_email(['', 'test']))  # Output: Second input must not be an empty string
print(generate_email(['one', 'two', 'three']))  # Output: Input list must contain exactly two elements
print(generate_email([123, 'test']))  # Output: Both inputs must be strings

# End time: 2024-03-30 02:33:27.068937
# Elapsed time in seconds: 6.945354392999434