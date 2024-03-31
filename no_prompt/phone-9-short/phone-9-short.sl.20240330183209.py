# Start time: 2024-03-30 18:43:29.022198

# Content: Given that given input as ['+106 769-858-438'] output is 106.769.858.438, given input as ['+83 973-757-831'] output is 83.973.757.831, given input as ['+62 647-787-775'] output is 62.647.787.775, given input as ['+172 027-507-632'] output is 172.027.507.632, given input as ['+72 001-050-856'] output is 72.001.050.856, given input as ['+95 310-537-401'] output is 95.310.537.401, given input as ['+6 775-969-238'] output is 6.775.969.238, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases
phone_numbers = ['+106 769-858-438', '+83 973-757-831', '+62 647-787-775', '+172 027-507-632', '+72 001-050-856', '+95 310-537-401', '+6 775-969-238']

# Function to format phone numbers
def format_phone_number(phone_number):
    try:
        # Remove all non-digit characters from the input phone number
        cleaned_number = ''.join(filter(str.isdigit, phone_number))
        
        # Insert dots at specific positions to format the phone number
        formatted_number = '.'.join([cleaned_number[:3], cleaned_number[3:6], cleaned_number[6:9], cleaned_number[9:]])
        
        return formatted_number
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Test the function with the given input
for number in phone_numbers:
    print(format_phone_number(number))

# End time: 2024-03-30 18:43:31.639325
# Elapsed time in seconds: 2.617053902999942