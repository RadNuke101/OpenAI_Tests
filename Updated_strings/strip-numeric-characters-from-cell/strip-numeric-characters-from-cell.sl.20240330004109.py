# Start time: 2024-03-30 00:49:53.910961
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: remove the numbers from input, and given input as ['34653 jim mcdonald'] output is  jim mcdonald, given input as ['price is 500'] output is  price is , given input as ['100 apples'] output is  apples, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: remove the numbers from input
# Input: '34653 jim mcdonald'
# Output: 'jim mcdonald'

# Input: 'price is 500'
# Output: 'price is'

# Input: '100 apples'
# Output: 'apples'

def remove_numbers(input_str):
    try:
        # Split the input string into words
        words = input_str.split()
        
        # Filter out words that do not contain any digits
        filtered_words = [word for word in words if not any(char.isdigit() for char in word)]
        
        # Join the filtered words back into a string
        output_str = ' '.join(filtered_words)
        
        return output_str
    except Exception as e:
        return str(e)

# Test cases
print(remove_numbers('34653 jim mcdonald'))  # Output: jim mcdonald
print(remove_numbers('price is 500'))         # Output: price is
print(remove_numbers('100 apples'))           # Output: apples

# End time: 2024-03-30 00:49:56.437001
# Elapsed time in seconds: 2.525975831999858