# Start time: 2024-03-30 20:54:26.185154

# Content: Given that given input as ['+106 769-858-438'] output is +106 (769) 858-438, given input as ['+83 973-757-831'] output is +83 (973) 757-831, given input as ['+62 647-787-775'] output is +62 (647) 787-775, given input as ['+172 027-507-632'] output is +172 (027) 507-632, given input as ['+72 001-050-856'] output is +72 (001) 050-856, given input as ['+95 310-537-401'] output is +95 (310) 537-401, given input as ['+6 775-969-238'] output is +6 (775) 969-238, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def format_phone_number(phone_number):
    try:
        # Input: '+106 769-858-438'  Output: +106 (769) 858-438
        # Input: '+83 973-757-831'   Output: +83 (973) 757-831
        # Input: '+62 647-787-775'   Output: +62 (647) 787-775
        # Input: '+172 027-507-632'  Output: +172 (027) 507-632
        # Input: '+72 001-050-856'   Output: +72 (001) 050-856
        # Input: '+95 310-537-401'   Output: +95 (310) 537-401
        # Input: '+6 775-969-238'    Output: +6 (775) 969-238
        
        # Remove any leading or trailing whitespaces
        phone_number = phone_number.strip()
        
        # Split the phone number into country code, area code, and number
        parts = phone_number.split()
        country_code = parts[0]
        area_code = parts[1].replace('-', '')
        number = parts[2].replace('-', '')
        
        # Format the phone number
        formatted_number = f"{country_code} ({area_code}) {number}"
        
        return formatted_number
        
    except Exception as e:
        print(f"Error: {e}")
        return None

# Test cases
print(format_phone_number('+106 769-858-438'))  # Output: +106 (769) 858-438
print(format_phone_number('+83 973-757-831'))   # Output: +83 (973) 757-831
print(format_phone_number('+62 647-787-775'))   # Output: +62 (647) 787-775
print(format_phone_number('+172 027-507-632'))  # Output: +172 (027) 507-632
print(format_phone_number('+72 001-050-856'))   # Output: +72 (001) 050-856
print(format_phone_number('+95 310-537-401'))   # Output: +95 (310) 537-401
print(format_phone_number('+6 775-969-238'))    # Output: +6 (775) 969-238

# End time: 2024-03-30 20:54:29.840262
# Elapsed time in seconds: 3.655014076999578