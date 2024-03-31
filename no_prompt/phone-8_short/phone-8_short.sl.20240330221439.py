# Start time: 2024-03-30 22:18:09.505732

# Content: Given that given input as ['+106 769-858-438'] output is 438, given input as ['+83 973-757-831'] output is 831, given input as ['+62 647-787-775'] output is 775, given input as ['+172 027-507-632'] output is 632, given input as ['+72 001-050-856'] output is 856, given input as ['+95 310-537-401'] output is 401, given input as ['+6 775-969-238'] output is 238, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: '+106 769-858-438', output: 438
# input: '+83 973-757-831', output: 831
# input: '+62 647-787-775', output: 775
# input: '+172 027-507-632', output: 632
# input: '+72 001-050-856', output: 856
# input: '+95 310-537-401', output: 401
# input: '+6 775-969-238', output: 238

def extract_last_number(input_str):
    try:
        number = input_str.split('-')[-1]
        return int(number)
    except (IndexError, ValueError):
        return None

# Test the function with the provided test cases
print(extract_last_number('+106 769-858-438'))  # 438
print(extract_last_number('+83 973-757-831'))   # 831
print(extract_last_number('+62 647-787-775'))   # 775
print(extract_last_number('+172 027-507-632'))  # 632
print(extract_last_number('+72 001-050-856'))   # 856
print(extract_last_number('+95 310-537-401'))   # 401
print(extract_last_number('+6 775-969-238'))    # 238

# End time: 2024-03-30 22:18:14.704130
# Elapsed time in seconds: 5.198259071999928