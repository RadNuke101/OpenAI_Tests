# Start time: 2024-03-30 01:40:50.230904
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: remove numbers from first input, and given input as ['80v', '3'] output is v, given input as ['10hrs', '3'] output is hrs, given input as ['7h', '2'] output is h, given input as ['500m', '4'] output is m, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: remove numbers from first input
# Input: ['80v', '3']
# Output: v

def remove_numbers(input_str):
    try:
        # Split the input into the string and number parts
        string_part, num_part = input_str.split(' ')
        
        # Remove numbers from the string part
        result = ''.join([char for char in string_part if not char.isdigit()])
        
        return result
    except ValueError:
        return "Invalid input format"

# Test cases
print(remove_numbers('80v 3'))  # Output: v
print(remove_numbers('10hrs 3'))  # Output: hrs
print(remove_numbers('7h 2'))  # Output: h
print(remove_numbers('500m 4'))  # Output: m

# End time: 2024-03-30 01:40:54.118066
# Elapsed time in seconds: 3.8870859910002764