# Start time: 2024-04-10 14:28:51.812080

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: The input data consists of phone numbers in the format '+XX XXX-XXX-XXX', where XX represents the country code, the first set of XXX represents the area code, and the last set of XXX represents the specific phone number. The output data is the last set of XXX from each input.

Summary for Input Data:
- The input data consists of phone numbers from various countries.
- Each phone number is formatted as '+XX XXX-XXX-XXX'.
- The country code, area code, and specific phone number are separated by spaces and hyphens.

Summary for Output Data:
- The output data consists of the last set of XXX from each input phone number.
- The output represents the specific phone number within each input.
- The output is the final set of digits that uniquely identifies each phone number.

Relationship between Input and Output:
- The output represents the unique identifier within each input phone number.
- The output is extracted from the input data by focusing on the last set of XXX.
- The relationship between the input and output is that the output is a specific part of the input that distinguishes one phone number from another., and input as ['+106 769-858-438'] output is 438, input as ['+83 973-757-831'] output is 831, input as ['+62 647-787-775'] output is 775, input as ['+172 027-507-632'] output is 632, input as ['+72 001-050-856'] output is 856, input as ['+95 310-537-401'] output is 401, input as ['+6 775-969-238'] output is 238, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(*args):
    outputs = []
    for arg in args:
        output = arg.split('-')[-1]
        outputs.append(output)
    return outputs

# Test cases
generated_function('+106 769-858-438', '+83 973-757-831', '+62 647-787-775', '+172 027-507-632', '+72 001-050-856', '+95 310-537-401', '+6 775-969-238')
print(generated_function("+106 769-858-438"))  ## Output: 438
print(generated_function("+83 973-757-831"))  ## Output: 831
print(generated_function("+62 647-787-775"))  ## Output: 775
print(generated_function("+172 027-507-632"))  ## Output: 632
print(generated_function("+72 001-050-856"))  ## Output: 856
print(generated_function("+95 310-537-401"))  ## Output: 401
print(generated_function("+6 775-969-238"))  ## Output: 238

# End time: 2024-04-10 14:28:53.904585
# Elapsed time in seconds: 2.092458985999997