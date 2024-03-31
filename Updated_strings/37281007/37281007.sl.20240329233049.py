# Start time: 2024-03-29 23:45:43.809589
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if entered letter or phrase (second column) is in the expression (first column), return true, else false, and given input as ['ABC', 'D'] output is false, given input as ['ABC', 'BC'] output is true, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: if entered letter or phrase (second column) is in the expression (first column), return true, else false
# Input: ['ABC', 'D'] 
# Output: false
# Input: ['ABC', 'BC'] 
# Output: true

def check_match(expression, letter):
    try:
        return letter in expression
    except Exception as e:
        print("Error:", e)
        return None

# Test cases
print(check_match('ABC', 'D'))  # Output: False
print(check_match('ABC', 'BC'))  # Output: True

# End time: 2024-03-29 23:45:46.212915
# Elapsed time in seconds: 2.403254215000061