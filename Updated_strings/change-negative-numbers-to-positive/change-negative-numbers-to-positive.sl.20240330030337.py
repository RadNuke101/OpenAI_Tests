# Start time: 2024-03-30 03:10:20.158873
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if "-" present in the beginning of inputted expression (first column), remove it, and given input as ['-%134'] output is %134, given input as ['500'] output is 500, given input as ['5.125'] output is 5.125, given input as ['-%43.00'] output is %43.00, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: if "-" present in the beginning of inputted expression, remove it
# Input: '-%134'  Output: %134
# Input: '500'  Output: 500
# Input: '5.125'  Output: 5.125
# Input: '-%43.00'  Output: %43.00

def remove_minus(input_str):
    try:
        if input_str.startswith('-'):
            return input_str[1:]
        else:
            return input_str
    except Exception as e:
        return "Error: " + str(e)

# Test cases
print(remove_minus('-%134'))  # Output: %134
print(remove_minus('500'))    # Output: 500
print(remove_minus('5.125'))  # Output: 5.125
print(remove_minus('-%43.00'))  # Output: %43.00

# End time: 2024-03-30 03:10:25.685588
# Elapsed time in seconds: 5.526564464998955