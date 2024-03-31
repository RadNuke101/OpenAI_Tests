# Start time: 2024-03-30 20:01:35.029837

# Content: Given that given input as ['+106 769-858-438'] output is 106.769.858.438, given input as ['+83 973-757-831'] output is 83.973.757.831, given input as ['+62 647-787-775'] output is 62.647.787.775, given input as ['+172 027-507-632'] output is 172.027.507.632, given input as ['+72 001-050-856'] output is 72.001.050.856, given input as ['+95 310-537-401'] output is 95.310.537.401, given input as ['+6 775-969-238'] output is 6.775.969.238, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases
phone_numbers = ['+106 769-858-438', '+83 973-757-831', '+62 647-787-775', '+172 027-507-632', '+72 001-050-856', '+95 310-537-401', '+6 775-969-238']

# Function to format phone number
def format_phone_number(phone):
    try:
        # Remove all non-digit characters from the input phone number
        phone = ''.join(filter(str.isdigit, phone))
        
        # Insert dots at specific positions to format the phone number
        formatted_phone = '.'.join([phone[:3], phone[3:6], phone[6:9], phone[9:]])
        
        return formatted_phone
    except Exception as e:
        return str(e)

# Test the function with the provided input
for phone_number in phone_numbers:
    print(format_phone_number(phone_number))

# End time: 2024-03-30 20:01:39.434846
# Elapsed time in seconds: 4.404932904999441