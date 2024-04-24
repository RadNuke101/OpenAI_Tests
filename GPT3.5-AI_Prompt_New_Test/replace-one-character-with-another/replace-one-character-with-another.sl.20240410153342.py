# Start time: 2024-04-10 15:43:52.627657

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
- The input column data consists of phone numbers in the format XXX XXX XXXX, where each group of numbers is separated by a space.

Summary for Output Column:
- The output column consists of phone numbers in the format XXX-XXX-XXXX, where each group of numbers is separated by a hyphen.

Relationship between Input and Output:
- The relationship between the input and output is that the input phone numbers are transformed from a space-separated format to a hyphen-separated format in the output. This transformation involves changing the separator between the groups of numbers while keeping the numbers themselves unchanged., and input as ['801 456 8756'] output is 801-456-8756, input as ['978 456 8756'] output is 978-456-8756, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(input_str):
    # Split the input string by space
    input_list = input_str.split()
    
    # Join the elements of the input list with hyphens
    output_str = '-'.join(input_list)
    
    # Return the output string
    return output_str

# Test cases
print(generated_function('801 456 8756')) # Output: 801-456-8756
print(generated_function('978 456 8756')) # Output: 978-456-8756
print(generated_function("801 456 8756"))  ## Output: 801-456-8756
print(generated_function("978 456 8756"))  ## Output: 978-456-8756

# End time: 2024-04-10 15:43:54.758265
# Elapsed time in seconds: 2.1305607349995626


# APPEND TEST SCRIPTS...
print(generated_function("801 456 8756"))  ## Output: 801-456-8756
print(generated_function("978 456 8756"))  ## Output: 978-456-8756


print(generated_function("456 801 8756"))  ### Output: 456-801-8756
print(generated_function("456 978 8756"))  ### Output: 456-978-8756

# TEST SCRIPTS APPENDED!

