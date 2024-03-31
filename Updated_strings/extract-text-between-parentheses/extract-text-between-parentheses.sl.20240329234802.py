# Start time: 2024-03-29 23:56:01.079168
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the text between "<" and ">" in the inputted expression, and given input as ['Jones <60>'] output is 60, given input as ['Jones <57>'] output is 57, given input as ['Jones <55>'] output is 55, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the text between "<" and ">" in the inputted expression
# Input: 'Jones <60>'
# Output: '60'

def extract_text(input_str):
    try:
        start_index = input_str.index("<") + 1
        end_index = input_str.index(">")
        return input_str[start_index:end_index]
    except ValueError:
        return "Invalid input format"

# Test cases
print(extract_text('Jones <60>'))  # Output: '60'
print(extract_text('Jones <57>'))  # Output: '57'
print(extract_text('Jones <55>'))  # Output: '55'

# End time: 2024-03-29 23:56:03.110146
# Elapsed time in seconds: 2.030682246999959