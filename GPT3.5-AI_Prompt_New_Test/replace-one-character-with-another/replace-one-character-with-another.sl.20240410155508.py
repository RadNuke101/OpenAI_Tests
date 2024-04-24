# Start time: 2024-04-10 16:05:35.740925

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
- The input column data consists of phone numbers in the format XXX XXX XXXX, where each group of numbers is separated by a space.
- The numbers in the input column data represent phone numbers with area code, prefix, and line number.

Summary for Output Column:
- The output column data consists of phone numbers in the format XXX-XXX-XXXX, where each group of numbers is separated by a hyphen.
- The output column data represents formatted phone numbers with area code, prefix, and line number.

Relationship between Input and Output:
- The relationship between the input and output is that the input phone numbers are being reformatted to have hyphens instead of spaces between the groups of numbers.
- The transformation from input to output involves a simple formatting change to make the phone numbers more visually appealing and easier to read.
- The output maintains the same information as the input but presents it in a standardized format., and input as ['801 456 8756'] output is 801-456-8756, input as ['978 456 8756'] output is 978-456-8756, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(input_str):
    # Split the input string into groups of numbers
    groups = input_str.split()
    
    # Reformat the phone number with hyphens
    output = '-'.join(groups)
    
    return output

# Test cases
print(generated_function('801 456 8756')) # Output: 801-456-8756
print(generated_function('978 456 8756')) # Output: 978-456-8756
print(generated_function("801 456 8756"))  ## Output: 801-456-8756
print(generated_function("978 456 8756"))  ## Output: 978-456-8756

# End time: 2024-04-10 16:05:37.473717
# Elapsed time in seconds: 1.7327504029999545


# APPEND TEST SCRIPTS...
print(generated_function("801 456 8756"))  ## Output: 801-456-8756
print(generated_function("978 456 8756"))  ## Output: 978-456-8756


print(generated_function("456 801 8756"))  ### Output: 456-801-8756
print(generated_function("456 978 8756"))  ### Output: 456-978-8756

# TEST SCRIPTS APPENDED!

