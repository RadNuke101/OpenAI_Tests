# Start time: 2024-03-30 02:15:51.208869
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: remove numbers from first input, and given input as ['apples30', '7'] output is apples, given input as ['peaches24', '8'] output is peaches, given input as ['peaches0', '8'] output is peaches, given input as ['pears', '6'] output is pears, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: remove numbers from first input
# Input: ['apples30', '7'] 
# Output: apples

def remove_numbers(input_str):
    try:
        # Extract the first element from the input string
        input_str = input_str.split(',')[0]
        
        # Remove numbers from the input string
        output_str = ''.join([char for char in input_str if not char.isdigit()])
        
        return output_str
    except Exception as e:
        return "Error: " + str(e)

# Test cases
print(remove_numbers('apples30, 7'))  # Output: apples
print(remove_numbers('peaches24, 8'))  # Output: peaches
print(remove_numbers('peaches0, 8'))   # Output: peaches
print(remove_numbers('pears, 6'))      # Output: pears

# End time: 2024-03-30 02:15:53.803494
# Elapsed time in seconds: 2.5945730289986386