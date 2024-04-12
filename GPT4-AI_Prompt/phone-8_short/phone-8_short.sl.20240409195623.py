# Start time: 2024-04-09 20:20:48.237982

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Summary of Input Column Data

The input data consists of strings that follow a specific format representing phone numbers. Each string begins with a country code prefixed with a plus sign ('+'), followed by a space, and then a sequence of digits separated by hyphens into three groups. The format can be summarized as `+CC XXX-XXX-XXX`, where `CC` represents the country code which can vary in length, and the three groups of `XXX` represent the local number parts. The country codes and the local number parts vary across the dataset, indicating a diverse set of phone numbers from different regions. The input data is qualitative, as it represents categories (different phone numbers) rather than numerical values that can be manipulated mathematically.

### Summary of Output Column Data

The output data consists of integers extracted from the last group of digits in the input strings. These integers range from 238 to 856, based on the provided examples. The output represents the last segment of the local phone number from the input data. This segment is always a three-digit number, based on the examples provided. The output data is quantitative, as it consists of numerical values that can be subject to mathematical operations.

### Relationship Between Input and Output

The relationship between the input and output data is direct and systematic. The output is derived from the input by extracting the last group of digits from the phone number represented in the input string. Specifically, the output is the last three digits of the local number part of the phone number, following the last hyphen in the input string. This extraction process treats the input data qualitatively, identifying a specific pattern within the string, and then converting a part of this pattern into a quantitative output value. The process highlights a transformation from a qualitative representation of phone numbers to a quantitative representation focusing on the last segment of these numbers., and input as ['+106 769-858-438'] output is 438, input as ['+83 973-757-831'] output is 831, input as ['+62 647-787-775'] output is 775, input as ['+172 027-507-632'] output is 632, input as ['+72 001-050-856'] output is 856, input as ['+95 310-537-401'] output is 401, input as ['+6 775-969-238'] output is 238, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    """
    Extracts the last three digits from the given phone number string.
    
    Args:
    - phone_number (str): A phone number string in the format '+CC XXX-XXX-XXX'.
    
    Returns:
    - int: The last three digits of the local phone number.
    """
    # Extract the last segment after the last hyphen which represents the last three digits
    last_segment = phone_number.split('-')[-1]
    return int(last_segment)

# Test cases
print(generated_function('+106 769-858-438'))  # Expected output: 438
print(generated_function('+83 973-757-831'))   # Expected output: 831
print(generated_function('+62 647-787-775'))   # Expected output: 775
print(generated_function('+172 027-507-632'))  # Expected output: 632
print(generated_function('+72 001-050-856'))   # Expected output: 856
print(generated_function('+95 310-537-401'))   # Expected output: 401
print(generated_function('+6 775-969-238'))    # Expected output: 238
print(generated_function("+106 769-858-438"))  ## Output: 438
print(generated_function("+83 973-757-831"))  ## Output: 831
print(generated_function("+62 647-787-775"))  ## Output: 775
print(generated_function("+172 027-507-632"))  ## Output: 632
print(generated_function("+72 001-050-856"))  ## Output: 856
print(generated_function("+95 310-537-401"))  ## Output: 401
print(generated_function("+6 775-969-238"))  ## Output: 238

# End time: 2024-04-09 20:20:59.259109
# Elapsed time in seconds: 11.020889231000183