# Start time: 2024-03-30 19:58:10.762925

# Content: Given that given input as ['801 456 8756'] output is 801-456-8756, given input as ['978 456 8756'] output is 978-456-8756, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: '801 456 8756'
# Output: 801-456-8756

def format_phone_number(input_str):
    try:
        # Split the input string by space
        parts = input_str.split()
        
        # Check if there are exactly 3 parts
        if len(parts) != 3:
            raise ValueError("Input must contain exactly 3 parts separated by space")
        
        # Join the parts with hyphens
        formatted_number = "-".join(parts)
        
        return formatted_number
    except Exception as e:
        return str(e)

# Test cases
print(format_phone_number('801 456 8756'))  # Output: 801-456-8756
print(format_phone_number('978 456 8756'))  # Output: 978-456-8756
print(format_phone_number('123 456'))      # Output: Input must contain exactly 3 parts separated by space
print(format_phone_number('123 456 789 1011'))  # Output: Input must contain exactly 3 parts separated by space

# End time: 2024-03-30 19:58:13.562358
# Elapsed time in seconds: 2.7993875729998763