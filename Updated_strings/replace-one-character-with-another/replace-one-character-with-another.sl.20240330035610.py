# Start time: 2024-03-30 04:04:00.191438
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: replaces spaces in input with "-", and given input as ['801 456 8756'] output is 801-456-8756, given input as ['978 456 8756'] output is 978-456-8756, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: replaces spaces in input with "-", and given input as ['801 456 8756'] output is 801-456-8756, given input as ['978 456 8756'] output is 978-456-8756

def replace_spaces_with_dash(input_str):
    try:
        if not isinstance(input_str, str):
            raise ValueError("Input must be a string")
        
        output_str = input_str.replace(" ", "-")
        
        return output_str
    except Exception as e:
        return str(e)

# Test cases
print(replace_spaces_with_dash('801 456 8756'))  # Output: 801-456-8756
print(replace_spaces_with_dash('978 456 8756'))  # Output: 978-456-8756
print(replace_spaces_with_dash(123))  # Output: Input must be a string

# End time: 2024-03-30 04:04:03.245218
# Elapsed time in seconds: 3.053727271999378