# Start time: 2024-03-30 23:12:30.107269

# Content: Given that given input as ['+106 769-858-438'] output is 438, given input as ['+83 973-757-831'] output is 831, given input as ['+62 647-787-775'] output is 775, given input as ['+172 027-507-632'] output is 632, given input as ['+72 001-050-856'] output is 856, given input as ['+95 310-537-401'] output is 401, given input as ['+6 775-969-238'] output is 238, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: '+106 769-858-438', output: '438'
# input: '+83 973-757-831', output: '831'
# input: '+62 647-787-775', output: '775'
# input: '+172 027-507-632', output: '632'
# input: '+72 001-050-856', output: '856'
# input: '+95 310-537-401', output: '401'
# input: '+6 775-969-238', output: '238'

def extract_last_number(input_str):
    try:
        # Split the input string by '-'
        parts = input_str.split('-')
        
        # Get the last part and extract the last number
        last_part = parts[-1]
        last_number = last_part.split()[-1]
        
        return last_number
    except Exception as e:
        print(f"Error: {e}")
        return None

# Test the function with the provided test cases
print(extract_last_number('+106 769-858-438'))  # Output: 438
print(extract_last_number('+83 973-757-831'))   # Output: 831
print(extract_last_number('+62 647-787-775'))   # Output: 775
print(extract_last_number('+172 027-507-632'))  # Output: 632
print(extract_last_number('+72 001-050-856'))   # Output: 856
print(extract_last_number('+95 310-537-401'))   # Output: 401
print(extract_last_number('+6 775-969-238'))    # Output: 238

# End time: 2024-03-30 23:12:33.710674
# Elapsed time in seconds: 3.6032974010013277