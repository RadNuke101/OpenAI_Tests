# Start time: 2024-03-30 20:04:35.923787

# Content: Given that given input as ['Dec 2, 2014, 11=23 PM - +91 90000 80000= loren ipsum'] output is loren ipsum, given input as ['Dec 2, 2014, 11=24 PM - +91 90000 80000= loren'] output is loren, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_text(input_string):
    try:
        # Input: 'Dec 2, 2014, 11=23 PM - +91 90000 80000= loren ipsum'
        # Output: 'loren ipsum'
        
        parts = input_string.split('=')
        text = parts[-1].strip()
        
        return text
    except Exception as e:
        print("Error: {}".format(e))

# Test cases
input1 = 'Dec 2, 2014, 11=23 PM - +91 90000 80000= loren ipsum'
input2 = 'Dec 2, 2014, 11=24 PM - +91 90000 80000= loren'

output1 = extract_text(input1)
output2 = extract_text(input2)

# End time: 2024-03-30 20:04:38.308045
# Elapsed time in seconds: 2.3842238380002527