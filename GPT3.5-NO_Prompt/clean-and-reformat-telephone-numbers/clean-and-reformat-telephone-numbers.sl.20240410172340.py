# Start time: 2024-04-10 17:24:31.741134

'''
Prompt:
Given that input as ['801-456-8765'] output is 8014568765, input as ['<978> 654-0299'] output is 9786540299, input as ['978.654.0299'] output is 9786540299, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        phone_num = ''
        for char in input_str:
            if char.isdigit():
                phone_num += char
        return phone_num
    except Exception as e:
        return "Invalid input"

# Test cases
print(generated_function('801-456-8765'))
print(generated_function('<978> 654-0299'))
print(generated_function('978.654.0299'))
print(generated_function("801-456-8765"))  ## Output: 8014568765
print(generated_function("<978> 654-0299"))  ## Output: 9786540299
print(generated_function("978.654.0299"))  ## Output: 9786540299

# End time: 2024-04-10 17:24:33.004586
# Elapsed time in seconds: 1.2634248769999985