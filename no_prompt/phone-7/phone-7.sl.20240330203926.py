# Start time: 2024-03-30 20:40:07.787201

# Content: Given that given input as ['+106 769-858-438'] output is 858, given input as ['+83 973-757-831'] output is 757, given input as ['+62 647-787-775'] output is 787, given input as ['+172 027-507-632'] output is 507, given input as ['+72 001-050-856'] output is 050, given input as ['+95 310-537-401'] output is 537, given input as ['+6 775-969-238'] output is 969, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: '+106 769-858-438', output: 858
# input: '+83 973-757-831', output: 757
# input: '+62 647-787-775', output: 787
# input: '+172 027-507-632', output: 507
# input: '+72 001-050-856', output: 050
# input: '+95 310-537-401', output: 537
# input: '+6 775-969-238', output: 969

def extract_middle_number(phone_number):
    try:
        # Split the phone number by '-'
        parts = phone_number.split('-')
        
        # Extract the middle part and remove any leading zeros
        middle_number = parts[1].lstrip('0')
        
        return middle_number
    except Exception as e:
        print(f"Error: {e}")
        return None

# Test the function with the provided test cases
print(extract_middle_number('+106 769-858-438'))
print(extract_middle_number('+83 973-757-831'))
print(extract_middle_number('+62 647-787-775'))
print(extract_middle_number('+172 027-507-632'))
print(extract_middle_number('+72 001-050-856'))
print(extract_middle_number('+95 310-537-401'))
print(extract_middle_number('+6 775-969-238'))

# End time: 2024-03-30 20:40:14.013296
# Elapsed time in seconds: 6.225936989999354