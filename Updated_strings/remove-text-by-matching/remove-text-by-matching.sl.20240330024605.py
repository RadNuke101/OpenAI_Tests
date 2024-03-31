# Start time: 2024-03-30 02:51:13.976807
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: remove all instances of "-" from input, and given input as ['801-345-1987'] output is 8013451987, given input as ['612-554-2000'] output is 6125542000, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: remove all instances of "-" from input
# Input: '801-345-1987'
# Output: '8013451987'

def remove_dashes(input_str):
    try:
        output_str = input_str.replace("-", "")
        return output_str
    except AttributeError:
        return "Invalid input, please provide a valid string"

# Test cases
print(remove_dashes('801-345-1987'))  # Output: '8013451987'
print(remove_dashes('612-554-2000'))  # Output: '6125542000'
print(remove_dashes('123-456-7890'))  # Output: '1234567890'
print(remove_dashes('abc-def-ghij'))  # Output: 'abcdefghij'
print(remove_dashes(1234567890))      # Output: 'Invalid input, please provide a valid string'

# End time: 2024-03-30 02:51:17.527826
# Elapsed time in seconds: 3.5509404229997017