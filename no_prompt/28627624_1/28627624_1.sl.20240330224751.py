# Start time: 2024-03-30 22:50:07.116072

# Content: Given that given input as ['Dec 2, 2014, 11=23 PM - +91 90000 80000= loren ipsum'] output is Dec 2, 2014, 11=23 PM, given input as ['Dec 2, 2014, 11=24 PM - +91 90000 80000= loren'] output is Dec 2, 2014, 11=24 PM, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_date_time(input_str):
    try:
        # Input: 'Dec 2, 2014, 11=23 PM - +91 90000 80000= loren ipsum'
        # Output: 'Dec 2, 2014, 11=23 PM'
        
        # Split the input string by ' - ' to separate date/time part
        date_time_str = input_str.split(' - ')[0]
        
        return date_time_str
    except Exception as e:
        print(f"An error occurred: {e}")

# Test cases
input1 = 'Dec 2, 2014, 11=23 PM - +91 90000 80000= loren ipsum'
input2 = 'Dec 2, 2014, 11=24 PM - +91 90000 80000= loren'

output1 = extract_date_time(input1)
output2 = extract_date_time(input2)

print(output1)
print(output2)

# End time: 2024-03-30 22:50:10.513320
# Elapsed time in seconds: 3.3971651699994254