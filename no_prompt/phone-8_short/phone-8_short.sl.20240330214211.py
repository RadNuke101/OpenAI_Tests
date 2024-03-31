# Start time: 2024-03-30 21:47:08.783601

# Content: Given that given input as ['+106 769-858-438'] output is 438, given input as ['+83 973-757-831'] output is 831, given input as ['+62 647-787-775'] output is 775, given input as ['+172 027-507-632'] output is 632, given input as ['+72 001-050-856'] output is 856, given input as ['+95 310-537-401'] output is 401, given input as ['+6 775-969-238'] output is 238, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: '+106 769-858-438', output: 438
# input: '+83 973-757-831', output: 831
# input: '+62 647-787-775', output: 775
# input: '+172 027-507-632', output: 632
# input: '+72 001-050-856', output: 856
# input: '+95 310-537-401', output: 401
# input: '+6 775-969-238', output: 238

def extract_last_number(input_str):
    try:
        # Split the input string by '-' and get the last element
        last_number = input_str.split('-')[-1]
        return int(last_number)
    except (IndexError, ValueError):
        return None

# Test the function with the given test cases
test_cases = ['+106 769-858-438', '+83 973-757-831', '+62 647-787-775', '+172 027-507-632', '+72 001-050-856', '+95 310-537-401', '+6 775-969-238']
for test_case in test_cases:
    result = extract_last_number(test_case)
    print(f"Input: {test_case}, Output: {result}")

# End time: 2024-03-30 21:47:11.546298
# Elapsed time in seconds: 2.7626226950014825