# Start time: 2024-03-30 01:05:00.435697
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: remove numbers from first input, and given input as ['80v', '3'] output is v, given input as ['10hrs', '3'] output is hrs, given input as ['7h', '2'] output is h, given input as ['500m', '4'] output is m, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: remove numbers from first input
# Input: '80v', '3'
# Output: 'v'

def remove_numbers(input_str, num_str):
    try:
        input_str = input_str.replace(num_str, '')
        return input_str
    except:
        return "Invalid input"

# Test cases
print(remove_numbers('80v', '3'))  # Output: 'v'
print(remove_numbers('10hrs', '3'))  # Output: 'hrs'
print(remove_numbers('7h', '2'))  # Output: 'h'
print(remove_numbers('500m', '4'))  # Output: 'm'

# End time: 2024-03-30 01:05:03.181154
# Elapsed time in seconds: 2.745381036999788