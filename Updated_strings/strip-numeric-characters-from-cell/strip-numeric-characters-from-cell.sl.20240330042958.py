# Start time: 2024-03-30 04:40:26.495198
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: remove the numbers from input, and given input as ['34653 jim mcdonald'] output is  jim mcdonald, given input as ['price is 500'] output is  price is , given input as ['100 apples'] output is  apples, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: remove the numbers from input
# Input: '34653 jim mcdonald'
# Output: 'jim mcdonald'

# Input: 'price is 500'
# Output: 'price is'

# Input: '100 apples'
# Output: 'apples'

def remove_numbers(input_str):
    try:
        output_str = ''.join([char for char in input_str if not char.isdigit()])
        return output_str
    except Exception as e:
        print(f"An error occurred: {e}")

# Test cases
print(remove_numbers('34653 jim mcdonald'))  # Output: 'jim mcdonald'
print(remove_numbers('price is 500'))  # Output: 'price is'
print(remove_numbers('100 apples'))  # Output: 'apples'

# End time: 2024-03-30 04:40:29.839419
# Elapsed time in seconds: 3.344122120997781