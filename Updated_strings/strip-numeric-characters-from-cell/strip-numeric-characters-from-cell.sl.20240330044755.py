# Start time: 2024-03-30 04:57:38.436374
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: remove the numbers from input, and given input as ['34653 jim mcdonald'] output is  jim mcdonald, given input as ['price is 500'] output is  price is , given input as ['100 apples'] output is  apples, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: remove the numbers from input
# Input: ['34653 jim mcdonald']
# Output: jim mcdonald

def remove_numbers(input_str):
    try:
        input_str = input_str[0]  # Extract the string from the list
        output_str = ''.join([char for char in input_str if not char.isdigit()])  # Remove numbers from the input string
        return output_str
    except (IndexError, TypeError):
        return "Invalid input format"

# Test cases
print(remove_numbers(['34653 jim mcdonald']))  # Output: jim mcdonald
print(remove_numbers(['price is 500']))  # Output: price is
print(remove_numbers(['100 apples']))  # Output: apples

# End time: 2024-03-30 04:57:40.678208
# Elapsed time in seconds: 2.2418861240003025