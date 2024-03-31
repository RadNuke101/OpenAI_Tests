# Start time: 2024-03-30 18:24:17.127808

# Content: Given that given input as ['34653 jim mcdonald'] output is  jim mcdonald, given input as ['price is 500'] output is  price is , given input as ['100 apples'] output is  apples, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_last_word(input_str):
    try:
        # Input: '34653 jim mcdonald'
        # Output: 'jim mcdonald'
        words = input_str.split()
        last_word = words[-1]
        return last_word
    except IndexError:
        return ""
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

# Test cases
print(extract_last_word('34653 jim mcdonald'))  # Expected output: jim mcdonald
print(extract_last_word('price is 500'))  # Expected output: price is
print(extract_last_word('100 apples'))  # Expected output: apples

# End time: 2024-03-30 18:24:18.712821
# Elapsed time in seconds: 1.5849771609999834