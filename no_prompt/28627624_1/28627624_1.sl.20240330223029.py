# Start time: 2024-03-30 22:33:03.386849

# Content: Given that given input as ['Dec 2, 2014, 11=23 PM - +91 90000 80000= loren ipsum'] output is Dec 2, 2014, 11=23 PM, given input as ['Dec 2, 2014, 11=24 PM - +91 90000 80000= loren'] output is Dec 2, 2014, 11=24 PM, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_date_time(input_str):
    try:
        date_time = input_str.split(' - ')[0]
        return date_time
    except Exception as e:
        print("Error: {}".format(e))

# Test cases
input1 = 'Dec 2, 2014, 11=23 PM - +91 90000 80000= loren ipsum'
output1 = 'Dec 2, 2014, 11=23 PM'
print(extract_date_time(input1))

input2 = 'Dec 2, 2014, 11=24 PM - +91 90000 80000= loren'
output2 = 'Dec 2, 2014, 11=24 PM'
print(extract_date_time(input2))

# End time: 2024-03-30 22:33:05.044489
# Elapsed time in seconds: 1.65760184499959