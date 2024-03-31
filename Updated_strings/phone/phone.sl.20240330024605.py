# Start time: 2024-03-30 02:47:26.447531
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return first three numbers in input, and given input as ['938-242-504'] output is 938, given input as ['308-916-545'] output is 308, given input as ['623-599-749'] output is 623, given input as ['981-424-843'] output is 981, given input as ['118-980-214'] output is 118, given input as ['244-655-094'] output is 244, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return first three numbers in input
# Input: '938-242-504'
# Output: 938

def get_first_three_numbers(input_str):
    try:
        # Split the input string by '-'
        numbers = input_str.split('-')
        
        # Return the first element of the list
        return int(numbers[0])
    except (IndexError, ValueError):
        return "Invalid input"

# Test cases
print(get_first_three_numbers('938-242-504'))  # Output: 938
print(get_first_three_numbers('308-916-545'))  # Output: 308
print(get_first_three_numbers('623-599-749'))  # Output: 623
print(get_first_three_numbers('981-424-843'))  # Output: 981
print(get_first_three_numbers('118-980-214'))  # Output: 118
print(get_first_three_numbers('244-655-094'))  # Output: 244

# End time: 2024-03-30 02:47:28.267663
# Elapsed time in seconds: 1.820096397999805