# Start time: 2024-03-29 23:40:19.192074
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: remove the numbers from input, and given input as ['34653 jim mcdonald'] output is  jim mcdonald, given input as ['price is 500'] output is  price is , given input as ['100 apples'] output is  apples, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: remove the numbers from input
# input: '34653 jim mcdonald'
# output: 'jim mcdonald'

# input: 'price is 500'
# output: 'price is'

# input: '100 apples'
# output: 'apples'

def remove_numbers(input_str):
    try:
        output_str = ''.join([char for char in input_str if not char.isdigit()])
        return output_str.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Test cases
print(remove_numbers('34653 jim mcdonald'))  # Output: 'jim mcdonald'
print(remove_numbers('price is 500'))        # Output: 'price is'
print(remove_numbers('100 apples'))          # Output: 'apples'

# End time: 2024-03-29 23:40:21.997040
# Elapsed time in seconds: 2.8048809879999226