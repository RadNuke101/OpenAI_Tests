# Start time: 2024-03-30 22:22:15.513573

# Content: Given that given input as ['801 456 8756'] output is 801-456-8756, given input as ['978 456 8756'] output is 978-456-8756, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def format_phone_number(input_str):
    try:
        # Convert input string to list of numbers
        num_list = input_str.split()
        
        # Format phone number
        formatted_num = "-".join(num_list)
        
        return formatted_num
    except Exception as e:
        return "Invalid input"

# Test cases
print(format_phone_number('801 456 8756'))  # Output should be 801-456-8756
print(format_phone_number('978 456 8756'))  # Output should be 978-456-8756

# End time: 2024-03-30 22:22:18.341540
# Elapsed time in seconds: 2.82788388300105