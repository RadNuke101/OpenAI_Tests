# Start time: 2024-03-29 23:53:03.021567
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: remove all instances of "-" from input, and given input as ['801-345-1987'] output is 8013451987, given input as ['612-554-2000'] output is 6125542000, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: remove all instances of "-" from input
# Input: '801-345-1987'
# Output: '8013451987'

def remove_dashes(input_str):
    try:
        output_str = input_str.replace("-", "")
        return output_str
    except AttributeError:
        return "Invalid input, please provide a string."

# Test cases
print(remove_dashes('801-345-1987'))  # Output: '8013451987'
print(remove_dashes('612-554-2000'))  # Output: '6125542000'
print(remove_dashes(12345))  # Output: 'Invalid input, please provide a string.'

# End time: 2024-03-29 23:53:05.557689
# Elapsed time in seconds: 2.536045346000037