# Start time: 2024-03-30 01:41:50.526280
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: replaces spaces in input with "-", and given input as ['801 456 8756'] output is 801-456-8756, given input as ['978 456 8756'] output is 978-456-8756, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: replaces spaces in input with "-", and given input as '801 456 8756' output is '801-456-8756', given input as '978 456 8756' output is '978-456-8756'

def replace_spaces_with_dash(input_str):
    try:
        output_str = input_str.replace(" ", "-")
        return output_str
    except AttributeError:
        return "Invalid input. Please provide a valid string."

# Test cases
print(replace_spaces_with_dash('801 456 8756'))  # Output: '801-456-8756'
print(replace_spaces_with_dash('978 456 8756'))  # Output: '978-456-8756'

# End time: 2024-03-30 01:41:52.703705
# Elapsed time in seconds: 2.1773820379994504