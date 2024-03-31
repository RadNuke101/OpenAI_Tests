# Start time: 2024-03-30 04:34:51.414441
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return expression after the space after the "=" sign, and given input as ['Name= ABC Retailers'] output is ABC Retailers, given input as [' ame= XYZ Suppliers'] output is XYZ Suppliers, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return expression after the space after the "=" sign
# Input: ['Name= ABC Retailers']
# Output: ABC Retailers

def get_expression(input_str):
    try:
        expression = input_str.split('=')[1].strip()
        return expression
    except IndexError:
        return "Invalid input format"

# Test cases
input1 = 'Name= ABC Retailers'
input2 = ' ame= XYZ Suppliers'

print(get_expression(input1))  # Output: ABC Retailers
print(get_expression(input2))  # Output: XYZ Suppliers

# End time: 2024-03-30 04:34:53.313369
# Elapsed time in seconds: 1.8988657349982532