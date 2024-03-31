# Start time: 2024-03-30 21:18:55.985307

# Content: Given that given input as ['+106 769-858-438'] output is 769, given input as ['+83 973-757-831'] output is 973, given input as ['+62 647-787-775'] output is 647, given input as ['+172 027-507-632'] output is 027, given input as ['+72 001-050-856'] output is 001, given input as ['+95 310-537-401'] output is 310, given input as ['+6 775-969-238'] output is 775, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_number(input_str):
    try:
        number = input_str.split()[1].split('-')[0]
        return number
    except IndexError:
        print("Invalid input format. Please provide input in the format '+XXX YYY-ZZZ-ZZZ' where XXX is the desired output number.")
        return None

# Test cases
# input: '+106 769-858-438', output: 769
print(extract_number('+106 769-858-438'))
# input: '+83 973-757-831', output: 973
print(extract_number('+83 973-757-831'))
# input: '+62 647-787-775', output: 647
print(extract_number('+62 647-787-775'))
# input: '+172 027-507-632', output: 027
print(extract_number('+172 027-507-632'))
# input: '+72 001-050-856', output: 001
print(extract_number('+72 001-050-856'))
# input: '+95 310-537-401', output: 310
print(extract_number('+95 310-537-401'))
# input: '+6 775-969-238', output: 775
print(extract_number('+6 775-969-238'))

# End time: 2024-03-30 21:18:58.775793
# Elapsed time in seconds: 2.790424868999253