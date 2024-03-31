# Start time: 2024-03-30 18:54:35.967451

# Content: Given that given input as ['+106 769-858-438'] output is 106.769.858.438, given input as ['+83 973-757-831'] output is 83.973.757.831, given input as ['+62 647-787-775'] output is 62.647.787.775, given input as ['+172 027-507-632'] output is 172.027.507.632, given input as ['+72 001-050-856'] output is 72.001.050.856, given input as ['+95 310-537-401'] output is 95.310.537.401, given input as ['+6 775-969-238'] output is 6.775.969.238, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: '+106 769-858-438', output: '106.769.858.438'
# input: '+83 973-757-831', output: '83.973.757.831'
# input: '+62 647-787-775', output: '62.647.787.775'
# input: '+172 027-507-632', output: '172.027.507.632'
# input: '+72 001-050-856', output: '72.001.050.856'
# input: '+95 310-537-401', output: '95.310.537.401'
# input: '+6 775-969-238', output: '6.775.969.238'

def format_phone_number(input_str):
    try:
        # Remove '+' and spaces from the input string
        input_str = input_str.replace('+', '').replace(' ', '')
        
        # Split the string into country code, area code, and phone number
        country_code = input_str[:3]
        area_code = input_str[3:6]
        phone_number = input_str[6:]
        
        # Format the phone number with periods
        formatted_number = f'{country_code}.{area_code}.{phone_number}'
        
        return formatted_number
    except Exception as e:
        print(f'Error: {e}')
        return None

# Test the function with the provided test cases
print(format_phone_number('+106 769-858-438'))
print(format_phone_number('+83 973-757-831'))
print(format_phone_number('+62 647-787-775'))
print(format_phone_number('+172 027-507-632'))
print(format_phone_number('+72 001-050-856'))
print(format_phone_number('+95 310-537-401'))
print(format_phone_number('+6 775-969-238'))

# End time: 2024-03-30 18:54:40.596315
# Elapsed time in seconds: 4.628749675000108