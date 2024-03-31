# Start time: 2024-03-30 04:51:38.134213
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the input, and given input as ['101'] output is 101, given input as ['1002'] output is 1002, given input as ['743'] output is 743, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the input, and given input as ['101'] output is 101, given input as ['1002'] output is 1002, given input as ['743'] output is 743

def return_input(input_str):
    try:
        output = input_str[0]  # Extract the first element from the input list
        return output
    except (IndexError, TypeError):
        return "Invalid input"

# Test cases
print(return_input(['101']))  # Output: 101
print(return_input(['1002']))  # Output: 1002
print(return_input(['743']))  # Output: 743
print(return_input('test'))  # Output: Invalid input
print(return_input(123))  # Output: Invalid input

# End time: 2024-03-30 04:51:39.759729
# Elapsed time in seconds: 1.6255164769972907