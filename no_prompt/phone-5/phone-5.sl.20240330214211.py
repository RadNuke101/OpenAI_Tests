# Start time: 2024-03-30 21:56:47.699378

# Content: Given that given input as ['+106 769-858-438'] output is 106, given input as ['+83 973-757-831'] output is 83, given input as ['+62 647-787-775'] output is 62, given input as ['+172 027-507-632'] output is 172, given input as ['+72 001-050-856'] output is 72, given input as ['+95 310-537-401'] output is 95, given input as ['+6 775-969-238'] output is 6, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_country_code(phone_number):
    try:
        country_code = phone_number.split()[0][1:]
        return int(country_code)
    except (ValueError, IndexError):
        return None

# Test cases
print(extract_country_code('+106 769-858-438'))  # Output: 106
print(extract_country_code('+83 973-757-831'))    # Output: 83
print(extract_country_code('+62 647-787-775'))    # Output: 62
print(extract_country_code('+172 027-507-632'))   # Output: 172
print(extract_country_code('+72 001-050-856'))    # Output: 72
print(extract_country_code('+95 310-537-401'))    # Output: 95
print(extract_country_code('+6 775-969-238'))     # Output: 6

# End time: 2024-03-30 21:56:51.331907
# Elapsed time in seconds: 3.632652649001102