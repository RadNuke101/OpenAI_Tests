# Start time: 2024-03-30 18:29:40.101571

# Content: Given that given input as ['+106 769-858-438'] output is 106, given input as ['+83 973-757-831'] output is 83, given input as ['+62 647-787-775'] output is 62, given input as ['+172 027-507-632'] output is 172, given input as ['+72 001-050-856'] output is 72, given input as ['+95 310-537-401'] output is 95, given input as ['+6 775-969-238'] output is 6, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: '+106 769-858-438', output: 106
# input: '+83 973-757-831', output: 83
# input: '+62 647-787-775', output: 62
# input: '+172 027-507-632', output: 172
# input: '+72 001-050-856', output: 72
# input: '+95 310-537-401', output: 95
# input: '+6 775-969-238', output: 6

def extract_country_code(phone_number):
    try:
        country_code = phone_number.split()[0][1:]
        return int(country_code)
    except (IndexError, ValueError):
        print("Invalid input format. Please provide a valid phone number.")
        return None

# Test the function with the provided test cases
print(extract_country_code('+106 769-858-438'))
print(extract_country_code('+83 973-757-831'))
print(extract_country_code('+62 647-787-775'))
print(extract_country_code('+172 027-507-632'))
print(extract_country_code('+72 001-050-856'))
print(extract_country_code('+95 310-537-401'))
print(extract_country_code('+6 775-969-238'))

# End time: 2024-03-30 18:29:42.290344
# Elapsed time in seconds: 2.1887111859999777