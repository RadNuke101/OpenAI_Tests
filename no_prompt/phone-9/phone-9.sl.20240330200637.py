# Start time: 2024-03-30 20:12:32.121681

# Content: Given that given input as ['+106 769-858-438'] output is 106.769.858.438, given input as ['+83 973-757-831'] output is 83.973.757.831, given input as ['+62 647-787-775'] output is 62.647.787.775, given input as ['+172 027-507-632'] output is 172.027.507.632, given input as ['+72 001-050-856'] output is 72.001.050.856, given input as ['+95 310-537-401'] output is 95.310.537.401, given input as ['+6 775-969-238'] output is 6.775.969.238, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: '+106 769-858-438', output: '106.769.858.438'
# input: '+83 973-757-831', output: '83.973.757.831'
# input: '+62 647-787-775', output: '62.647.787.775'
# input: '+172 027-507-632', output: '172.027.507.632'
# input: '+72 001-050-856', output: '72.001.050.856'
# input: '+95 310-537-401', output: '95.310.537.401'
# input: '+6 775-969-238', output: '6.775.969.238'

def format_phone_number(phone_number):
    try:
        # Remove all non-digit characters from the input string
        phone_number = ''.join(filter(str.isdigit, phone_number))
        
        # Insert dots at specific positions to format the phone number
        formatted_number = '.'.join([phone_number[:3], phone_number[3:6], phone_number[6:9], phone_number[9:]])
        
        return formatted_number
    except Exception as e:
        print(f"An error occurred: {e}")

# Test the function with the provided input
print(format_phone_number('+106 769-858-438'))
print(format_phone_number('+83 973-757-831'))
print(format_phone_number('+62 647-787-775'))
print(format_phone_number('+172 027-507-632'))
print(format_phone_number('+72 001-050-856'))
print(format_phone_number('+95 310-537-401'))
print(format_phone_number('+6 775-969-238'))

# End time: 2024-03-30 20:12:37.667262
# Elapsed time in seconds: 5.5455209029996695