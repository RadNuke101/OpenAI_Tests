# Start time: 2024-03-30 22:32:45.430523

# Content: Given that given input as ['801-456-8765'] output is 8014568765, given input as ['<978> 654-0299'] output is 9786540299, given input as ['978.654.0299'] output is 9786540299, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: '801-456-8765', output: 8014568765
# input: '<978> 654-0299', output: 9786540299
# input: '978.654.0299', output: 9786540299

def clean_phone_number(input_str):
    try:
        # Remove all non-digit characters from the input string
        clean_str = ''.join(filter(str.isdigit, input_str))
        return int(clean_str)
    except Exception as e:
        print("Error: ", e)
        return None

# Test the function with the provided test cases
print(clean_phone_number('801-456-8765'))
print(clean_phone_number('<978> 654-0299'))
print(clean_phone_number('978.654.0299'))

# End time: 2024-03-30 22:32:47.277559
# Elapsed time in seconds: 1.8469877399984398