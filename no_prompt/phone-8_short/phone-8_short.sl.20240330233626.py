# Start time: 2024-03-30 23:40:12.671449

# Content: Given that given input as ['+106 769-858-438'] output is 438, given input as ['+83 973-757-831'] output is 831, given input as ['+62 647-787-775'] output is 775, given input as ['+172 027-507-632'] output is 632, given input as ['+72 001-050-856'] output is 856, given input as ['+95 310-537-401'] output is 401, given input as ['+6 775-969-238'] output is 238, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# Input: '+106 769-858-438', Output: 438
# Input: '+83 973-757-831', Output: 831
# Input: '+62 647-787-775', Output: 775
# Input: '+172 027-507-632', Output: 632
# Input: '+72 001-050-856', Output: 856
# Input: '+95 310-537-401', Output: 401
# Input: '+6 775-969-238', Output: 238

def extract_last_number(input_str):
    try:
        number = input_str.split('-')[-1]
        return int(number)
    except (IndexError, ValueError):
        return None

# Test the function with the given inputs
print(extract_last_number('+106 769-858-438'))  # Output: 438
print(extract_last_number('+83 973-757-831'))   # Output: 831
print(extract_last_number('+62 647-787-775'))   # Output: 775
print(extract_last_number('+172 027-507-632'))  # Output: 632
print(extract_last_number('+72 001-050-856'))   # Output: 856
print(extract_last_number('+95 310-537-401'))   # Output: 401
print(extract_last_number('+6 775-969-238'))    # Output: 238

# End time: 2024-03-30 23:40:18.105423
# Elapsed time in seconds: 5.433889423002256