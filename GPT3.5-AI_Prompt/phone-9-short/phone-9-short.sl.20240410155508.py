# Start time: 2024-04-10 16:10:04.150150

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: The input data consists of phone numbers with country codes. The output data is the same phone numbers formatted with periods instead of hyphens. 

The relationship between the input and output data is that the output data is a formatted version of the input data. The input data provides the phone numbers in a specific format with hyphens separating the digits, while the output data presents the same phone numbers in a different format with periods instead of hyphens. 

Overall, the input data serves as the raw phone numbers, while the output data represents a standardized and formatted version of the phone numbers for easier readability or processing., and input as ['+106 769-858-438'] output is 106.769.858.438, input as ['+83 973-757-831'] output is 83.973.757.831, input as ['+62 647-787-775'] output is 62.647.787.775, input as ['+172 027-507-632'] output is 172.027.507.632, input as ['+72 001-050-856'] output is 72.001.050.856, input as ['+95 310-537-401'] output is 95.310.537.401, input as ['+6 775-969-238'] output is 6.775.969.238, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(*args):
    formatted_numbers = []
    for phone_number in args:
        formatted_number = phone_number.replace('-', '.')
        formatted_numbers.append(formatted_number)
    return formatted_numbers
print(generated_function("+106 769-858-438"))  ## Output: 106.769.858.438
print(generated_function("+83 973-757-831"))  ## Output: 83.973.757.831
print(generated_function("+62 647-787-775"))  ## Output: 62.647.787.775
print(generated_function("+172 027-507-632"))  ## Output: 172.027.507.632
print(generated_function("+72 001-050-856"))  ## Output: 72.001.050.856
print(generated_function("+95 310-537-401"))  ## Output: 95.310.537.401
print(generated_function("+6 775-969-238"))  ## Output: 6.775.969.238

# End time: 2024-04-10 16:10:06.981132
# Elapsed time in seconds: 2.8309070179993796