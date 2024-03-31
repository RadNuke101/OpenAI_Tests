# Start time: 2024-03-30 02:13:51.903656
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: take the first letter of the second input and add it to the front of the first input, then add "_acme.com" at the end , and given input as ['brown', 'traci'] output is tbrown_acme.com, given input as ['thomas', 'linda'] output is lthomas_acme.com, given input as ['ward', 'jack'] output is jward_acme.com, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: take the first letter of the second input and add it to the front of the first input, then add "_acme.com" at the end
# Input: ['brown', 'traci'] 
# Output: tbrown_acme.com

def generate_email(input_str):
    try:
        first_word, second_word = input_str.split()
        output = second_word[0] + first_word + "_acme.com"
        return output
    except ValueError:
        return "Input should contain two words separated by a space."

# Test cases
print(generate_email('brown traci'))  # Output: tbrown_acme.com
print(generate_email('thomas linda'))  # Output: lthomas_acme.com
print(generate_email('ward jack'))  # Output: jward_acme.com

# End time: 2024-03-30 02:13:54.397508
# Elapsed time in seconds: 2.493789702999493