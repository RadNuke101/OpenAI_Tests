# Start time: 2024-03-30 05:18:49.432875
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if the word "overhead" in expression, return false, else true, and given input as ['some project,other project'] output is true, given input as ['some project'] output is true, given input as ['overhead'] output is false, given input as ['some project, overhead'] output is false, given input as ['some project, other, boo'] output is true, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: if the word "overhead" in expression, return false, else true
# Input: 'some project,other project' Output: true
# Input: 'some project' Output: true
# Input: 'overhead' Output: false
# Input: 'some project, overhead' Output: false
# Input: 'some project, other, boo' Output: true

def check_expression(input_str):
    try:
        if 'overhead' in input_str:
            return 'false'
        else:
            return 'true'
    except Exception as e:
        return str(e)

# Test the function with sample inputs
print(check_expression('some project,other project'))  # Output: true
print(check_expression('some project'))  # Output: true
print(check_expression('overhead'))  # Output: false
print(check_expression('some project, overhead'))  # Output: false
print(check_expression('some project, other, boo'))  # Output: true

# End time: 2024-03-30 05:18:55.039305
# Elapsed time in seconds: 5.606429275001574