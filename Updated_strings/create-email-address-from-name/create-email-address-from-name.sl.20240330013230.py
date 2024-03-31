# Start time: 2024-03-30 01:38:08.214779
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: take the first letter of the second input and add it to the front of the first input, then add "_acme.com" at the end , and given input as ['brown', 'traci'] output is tbrown_acme.com, given input as ['thomas', 'linda'] output is lthomas_acme.com, given input as ['ward', 'jack'] output is jward_acme.com, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: take the first letter of the second input and add it to the front of the first input, then add "_acme.com" at the end
# Input: ['brown', 'traci'] Output: tbrown_acme.com
# Input: ['thomas', 'linda'] Output: lthomas_acme.com
# Input: ['ward', 'jack'] Output: jward_acme.com

def generate_email(input_list):
    try:
        first_input = input_list[0]
        second_input = input_list[1]
        
        if len(first_input) == 0 or len(second_input) == 0:
            raise ValueError("Inputs cannot be empty")
        
        email = second_input[0] + first_input + "_acme.com"
        return email
    except (IndexError, ValueError) as e:
        print(f"Error: {e}")
        return None

# Test cases
print(generate_email(['brown', 'traci']))  # Output: tbrown_acme.com
print(generate_email(['thomas', 'linda']))  # Output: lthomas_acme.com
print(generate_email(['ward', 'jack']))  # Output: jward_acme.com
print(generate_email(['', 'test']))  # Output: Error: Inputs cannot be empty
print(generate_email(['test', '']))  # Output: Error: Inputs cannot be empty
print(generate_email([]))  # Output: Error: list index out of range

# End time: 2024-03-30 01:38:14.731555
# Elapsed time in seconds: 6.516668104999553