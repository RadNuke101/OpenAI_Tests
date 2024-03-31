# Start time: 2024-03-30 21:56:34.750706

# Content: Given that given input as ['Dec 2, 2014, 11=23 PM - +91 90000 80000= loren ipsum'] output is loren ipsum, given input as ['Dec 2, 2014, 11=24 PM - +91 90000 80000= loren'] output is loren, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'Dec 2, 2014, 11=23 PM - +91 90000 80000= loren ipsum'
# Output: 'loren ipsum'

# Input: 'Dec 2, 2014, 11=24 PM - +91 90000 80000= loren'
# Output: 'loren'

def extract_text(input_str):
    try:
        # Split the input string by '='
        parts = input_str.split('=')
        
        # Get the last part after splitting by '=' and remove leading/trailing whitespaces
        result = parts[-1].strip()
        
        return result
    except Exception as e:
        print("Error occurred:", e)

# Test cases
input_str1 = 'Dec 2, 2014, 11=23 PM - +91 90000 80000= loren ipsum'
input_str2 = 'Dec 2, 2014, 11=24 PM - +91 90000 80000= loren'

output1 = extract_text(input_str1)
output2 = extract_text(input_str2)

# End time: 2024-03-30 21:56:38.837358
# Elapsed time in seconds: 4.087118675000966