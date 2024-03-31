# Start time: 2024-03-30 03:15:55.139779
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if the word "overhead" in expression, return false, else true, and given input as ['some project,other project'] output is true, given input as ['some project'] output is true, given input as ['overhead'] output is false, given input as ['some project, overhead'] output is false, given input as ['some project, other, boo'] output is true, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: if the word "overhead" in expression, return false, else true
# Input: ['some project,other project'] Output: true
# Input: ['some project'] Output: true
# Input: ['overhead'] Output: false
# Input: ['some project, overhead'] Output: false
# Input: ['some project, other, boo'] Output: true

def check_overhead(input_str):
    try:
        input_list = input_str.split(',')
        for item in input_list:
            if 'overhead' in item:
                return False
        return True
    except AttributeError:
        return "Invalid input format, please provide a string separated by commas"
    except Exception as e:
        return f"An error occurred: {e}"

# Test cases
print(check_overhead('some project,other project'))  # Output: True
print(check_overhead('some project'))  # Output: True
print(check_overhead('overhead'))  # Output: False
print(check_overhead('some project, overhead'))  # Output: False
print(check_overhead('some project, other, boo'))  # Output: True

# End time: 2024-03-30 03:15:58.896706
# Elapsed time in seconds: 3.756823808000263