# Start time: 2024-03-30 03:30:56.372841
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: From the left, delete the number (second input) of elements from the first input, and given input as ['1234', '1'] output is 234, given input as ['**512A', '2'] output is 512A, given input as ['343DMX', '3'] output is DMX, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: From the left, delete the number (second input) of elements from the first input
# Input: ['1234', '1'] Output: 234
# Input: ['**512A', '2'] Output: 512A
# Input: ['343DMX', '3'] Output: DMX

def delete_elements(input_list):
    try:
        input_str = input_list[0]
        num_elements = int(input_list[1])
        
        output_str = input_str[num_elements:]
        
        return output_str
    except (IndexError, ValueError):
        return "Invalid input format"

# Test cases
print(delete_elements(['1234', '1']))  # Output: 234
print(delete_elements(['**512A', '2']))  # Output: 512A
print(delete_elements(['343DMX', '3']))  # Output: DMX

# End time: 2024-03-30 03:31:03.660754
# Elapsed time in seconds: 7.287716466000347