# Start time: 2024-03-30 21:06:11.751393

# Content: Given that given input as ['+106 769-858-438'] output is 106.769.858.438, given input as ['+83 973-757-831'] output is 83.973.757.831, given input as ['+62 647-787-775'] output is 62.647.787.775, given input as ['+172 027-507-632'] output is 172.027.507.632, given input as ['+72 001-050-856'] output is 72.001.050.856, given input as ['+95 310-537-401'] output is 95.310.537.401, given input as ['+6 775-969-238'] output is 6.775.969.238, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# Input: '+106 769-858-438', Output: '106.769.858.438'
# Input: '+83 973-757-831', Output: '83.973.757.831'
# Input: '+62 647-787-775', Output: '62.647.787.775'
# Input: '+172 027-507-632', Output: '172.027.507.632'
# Input: '+72 001-050-856', Output: '72.001.050.856'
# Input: '+95 310-537-401', Output: '95.310.537.401'
# Input: '+6 775-969-238', Output: '6.775.969.238'

def format_phone_number(input_str):
    try:
        # Remove all non-digit characters from the input string
        clean_str = ''.join(filter(str.isdigit, input_str))
        
        # Insert periods at specific positions to format the phone number
        formatted_str = clean_str[:3] + '.' + clean_str[3:6] + '.' + clean_str[6:9] + '.' + clean_str[9:]
        
        return formatted_str
    except Exception as e:
        print(f"An error occurred: {e}")

# Test the function with the provided test cases
print(format_phone_number('+106 769-858-438'))
print(format_phone_number('+83 973-757-831'))
print(format_phone_number('+62 647-787-775'))
print(format_phone_number('+172 027-507-632'))
print(format_phone_number('+72 001-050-856'))
print(format_phone_number('+95 310-537-401'))
print(format_phone_number('+6 775-969-238'))

# End time: 2024-03-30 21:06:20.783232
# Elapsed time in seconds: 9.039070716000424