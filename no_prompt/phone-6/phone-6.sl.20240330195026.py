# Start time: 2024-03-30 19:54:52.576159

# Content: Given that given input as ['+106 769-858-438'] output is 769, given input as ['+83 973-757-831'] output is 973, given input as ['+62 647-787-775'] output is 647, given input as ['+172 027-507-632'] output is 027, given input as ['+72 001-050-856'] output is 001, given input as ['+95 310-537-401'] output is 310, given input as ['+6 775-969-238'] output is 775, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: '+106 769-858-438', output: 769
# input: '+83 973-757-831', output: 973
# input: '+62 647-787-775', output: 647
# input: '+172 027-507-632', output: 027
# input: '+72 001-050-856', output: 001
# input: '+95 310-537-401', output: 310
# input: '+6 775-969-238', output: 775

def extract_number(input_str):
    try:
        number = input_str.split()[1].split('-')[0]
        return number
    except IndexError:
        print("Invalid input format. Please provide input in the format '+XX YYY-ZZZ-ZZZ'")
        return None

# Test the function with the provided test cases
print(extract_number('+106 769-858-438'))
print(extract_number('+83 973-757-831'))
print(extract_number('+62 647-787-775'))
print(extract_number('+172 027-507-632'))
print(extract_number('+72 001-050-856'))
print(extract_number('+95 310-537-401'))
print(extract_number('+6 775-969-238'))

# End time: 2024-03-30 19:54:57.299978
# Elapsed time in seconds: 4.7237466360002145