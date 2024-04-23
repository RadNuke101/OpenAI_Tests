# Start time: 2024-04-09 17:16:27.767744

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Summary of Input Column Data

The input data consists of strings that follow a specific format: a "+" sign followed by a country code, a space, and then a phone number divided into three parts by hyphens. The country code varies in length, ranging from one to three digits. The phone number is consistently formatted as three groups of digits separated by hyphens. The first group, following the country code and space, appears to be the focus for extracting the output data. This group varies in length but is typically three digits long, though exceptions exist where it can be as short as two digits.

### Summary of Output Column Data

The output data extracted from the input strings is consistently the first group of digits in the phone number part, immediately following the country code and space. This group of digits is treated as a separate entity, regardless of its length, which can vary from two to three digits based on the provided examples. The output is considered as a qualitative piece of information extracted from the larger string, indicating a specific portion of the phone number that might have a particular significance or use in the given context.

### Relationship Between Input and Output

The relationship between the input and output data is a direct extraction process focused on a specific pattern within the input strings. The output is always the first group of digits of the phone number part, which follows the country code and a space in the input string. This process highlights a methodical approach to parsing and extracting specific information from a structured text format, treating the data qualitatively by focusing on the pattern and position of the digits within the string rather than their numerical value. The extraction process is consistent across all examples, indicating a clear, defined rule for determining the output from the given input., and input as ['+106 769-858-438'] output is 769, input as ['+83 973-757-831'] output is 973, input as ['+62 647-787-775'] output is 647, input as ['+172 027-507-632'] output is 027, input as ['+72 001-050-856'] output is 001, input as ['+95 310-537-401'] output is 310, input as ['+6 775-969-238'] output is 775, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    """
    Extracts the first group of digits in the phone number part from the given input string.
    
    Parameters:
    phone_number (str): A string formatted as "+<country code> <first group>-<second group>-<third group>".
    
    Returns:
    str: The first group of digits from the phone number part.
    """
    # Split the input string by space to separate the country code and the phone number
    parts = phone_number.split(' ')
    # Further split the phone number part by hyphen to isolate the groups of digits
    phone_parts = parts[1].split('-')
    # Return the first group of digits
    return phone_parts[0]

# Test cases
print(generated_function('+106 769-858-438'))  # Expected output: 769
print(generated_function('+83 973-757-831'))   # Expected output: 973
print(generated_function('+62 647-787-775'))   # Expected output: 647
print(generated_function('+172 027-507-632'))  # Expected output: 027
print(generated_function('+72 001-050-856'))   # Expected output: 001
print(generated_function('+95 310-537-401'))   # Expected output: 310
print(generated_function('+6 775-969-238'))    # Expected output: 775
print(generated_function("+106 769-858-438"))  ## Output: 769
print(generated_function("+83 973-757-831"))  ## Output: 973
print(generated_function("+62 647-787-775"))  ## Output: 647
print(generated_function("+172 027-507-632"))  ## Output: 027
print(generated_function("+72 001-050-856"))  ## Output: 001
print(generated_function("+95 310-537-401"))  ## Output: 310
print(generated_function("+6 775-969-238"))  ## Output: 775

# End time: 2024-04-09 17:16:37.674363
# Elapsed time in seconds: 9.906441719998838


# APPEND TEST SCRIPTS...
print(generated_function("+106 769-858-438"))  ## Output: 769
print(generated_function("+83 973-757-831"))  ## Output: 973
print(generated_function("+62 647-787-775"))  ## Output: 647
print(generated_function("+172 027-507-632"))  ## Output: 027
print(generated_function("+72 001-050-856"))  ## Output: 001
print(generated_function("+95 310-537-401"))  ## Output: 310
print(generated_function("+6 775-969-238"))  ## Output: 775


print(generated_function("+106 858-769-438"))  ### Output: 858
print(generated_function("+83 757-973-831"))  ### Output: 757
print(generated_function("+72 050-001-856"))  ### Output: 050
print(generated_function("+172 507-027-632"))  ### Output: 507
print(generated_function("+95 537-310-401"))  ### Output: 537
print(generated_function("+62 787-647-775"))  ### Output: 787
print(generated_function("+6 969-775-238"))  ### Output: 969

# TEST SCRIPTS APPENDED!

