# Start time: 2024-03-30 01:18:23.299610
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the last three numbers, and given input as ['938-242-504'] output is 504, given input as ['308-916-545'] output is 545, given input as ['623-599-749'] output is 749, given input as ['981-424-843'] output is 843, given input as ['118-980-214'] output is 214, given input as ['244-655-094'] output is 094, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the last three numbers
# Input: ['938-242-504'] Output: 504
# Input: ['308-916-545'] Output: 545
# Input: ['623-599-749'] Output: 749
# Input: ['981-424-843'] Output: 843
# Input: ['118-980-214'] Output: 214
# Input: ['244-655-094'] Output: 094

def return_last_three_numbers(input_str):
    try:
        # Extract the last three numbers from the input string
        output_str = input_str[-3:]
        return output_str
    except Exception as e:
        return f"Error: {e}"

# Test cases
print(return_last_three_numbers('938-242-504'))  # Output: 504
print(return_last_three_numbers('308-916-545'))  # Output: 545
print(return_last_three_numbers('623-599-749'))  # Output: 749
print(return_last_three_numbers('981-424-843'))  # Output: 843
print(return_last_three_numbers('118-980-214'))  # Output: 214
print(return_last_three_numbers('244-655-094'))  # Output: 094

# End time: 2024-03-30 01:18:26.331276
# Elapsed time in seconds: 3.0316110789999584