# Start time: 2024-04-10 15:43:04.311731

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: The input data consists of phone numbers in the format '+XXX XXX-XXX-XXX', where XXX represents numerical digits. The output is the last set of digits in each phone number.

Summary of Input Data:
- The input data consists of phone numbers with varying country codes (+XXX) and numerical digits separated by hyphens.
- Each phone number is unique and does not follow a specific pattern in terms of the numerical digits.
- The input data does not show any clear relationship or correlation between the country code, the numerical digits, or the hyphens.

Summary of Output Data:
- The output data consists of the last set of digits in each phone number.
- The output data shows a consistent pattern of being the last set of digits in each phone number.
- There is a direct relationship between the input data and the output data, where the output is derived from the input by extracting the last set of digits.

Relationship between Input and Output:
- The input data serves as the source from which the output data is derived by extracting the last set of digits.
- The output data is directly linked to the input data, as it represents a specific part of each phone number.
- The relationship between the input and output is based on the structure of the phone numbers, where the output is a consistent element extracted from the input.

Overall, the input data provides the context and structure for the output data, with the relationship between them being defined by the extraction of the last set of digits from each phone number., and input as ['+106 769-858-438'] output is 438, input as ['+83 973-757-831'] output is 831, input as ['+62 647-787-775'] output is 775, input as ['+172 027-507-632'] output is 632, input as ['+72 001-050-856'] output is 856, input as ['+95 310-537-401'] output is 401, input as ['+6 775-969-238'] output is 238, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(*args):
    outputs = []
    for phone_number in args:
        output = phone_number.split('-')[-1]
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

# End time: 2024-04-10 15:43:08.313794
# Elapsed time in seconds: 4.001965351999388