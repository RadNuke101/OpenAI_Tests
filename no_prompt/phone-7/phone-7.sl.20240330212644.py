# Start time: 2024-03-30 21:27:43.231264

# Content: Given that given input as ['+106 769-858-438'] output is 858, given input as ['+83 973-757-831'] output is 757, given input as ['+62 647-787-775'] output is 787, given input as ['+172 027-507-632'] output is 507, given input as ['+72 001-050-856'] output is 050, given input as ['+95 310-537-401'] output is 537, given input as ['+6 775-969-238'] output is 969, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_number(input_str):
    try:
        number = input_str.split('-')[1]
        return number
    except IndexError:
        print("Invalid input format. Input should be in the format '+XXX YYY-ZZZ-ZZZ'")
        return None

# Test cases
# input: '+106 769-858-438', output: '858'
# input: '+83 973-757-831', output: '757'
# input: '+62 647-787-775', output: '787'
# input: '+172 027-507-632', output: '507'
# input: '+72 001-050-856', output: '050'
# input: '+95 310-537-401', output: '537'
# input: '+6 775-969-238', output: '969'

# Uncomment the below code to test the function
# print(extract_number('+106 769-858-438'))
# print(extract_number('+83 973-757-831'))
# print(extract_number('+62 647-787-775'))
# print(extract_number('+172 027-507-632'))
# print(extract_number('+72 001-050-856'))
# print(extract_number('+95 310-537-401'))
# print(extract_number('+6 775-969-238'))

# End time: 2024-03-30 21:27:47.917650
# Elapsed time in seconds: 4.686258605999683