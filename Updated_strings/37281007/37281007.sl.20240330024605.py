# Start time: 2024-03-30 03:00:58.183892
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if entered letter or phrase (second column) is in the expression (first column), return true, else false, and given input as ['ABC', 'D'] output is false, given input as ['ABC', 'BC'] output is true, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: if entered letter or phrase (second column) is in the expression (first column), return true, else false
# Input: ['ABC', 'D'] 
# Output: false
# Input: ['ABC', 'BC'] 
# Output: true

def check_match(expression, check):
    try:
        return check in expression
    except Exception as e:
        print("An error occurred:", e)
        return False

# Test cases
print(check_match('ABC', 'D'))  # Output: False
print(check_match('ABC', 'BC'))  # Output: True

# End time: 2024-03-30 03:01:00.360733
# Elapsed time in seconds: 2.1767742000010912