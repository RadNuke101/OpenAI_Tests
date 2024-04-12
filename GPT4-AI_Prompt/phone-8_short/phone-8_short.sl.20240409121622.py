# Start time: 2024-04-09 12:47:46.063277

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: To summarize the relationship between the input and output data provided, we observe a pattern where each input consists of a string formatted as a phone number with an international dialing code prefix (e.g., "+106", "+83", "+62", etc.), followed by a sequence of numbers separated by dashes. The output is consistently the last three digits of the phone number, following the last dash in the input string.

### Input Column Summary:
- The input data is formatted as strings representing phone numbers.
- Each phone number includes an international dialing code prefix, starting with a "+" sign, followed by a space.
- The main part of the phone number is divided into three segments by dashes.
- The length of the segments between dashes and the international dialing code varies.
- The input data is qualitative, representing different phone numbers from potentially different countries or regions, as indicated by the varying international dialing codes.

### Output Column Summary:
- The output data consistently extracts the last segment of the phone number from the input, which is always a three-digit number.
- This output is quantitative, representing the last part of the phone number, but within the context of this dataset, it is treated as qualitative data due to its relationship with the input.
- The output does not depend on the international dialing code or the first two segments of the phone number but solely on the last segment.

### Relationship Summary:
- The relationship between the input and output is a direct extraction process, where the output is always the last three digits of the phone number provided in the input.
- This relationship indicates a pattern or rule that could be used to process similar data, where if given a phone number in a specific format, one can reliably extract the last three digits as the output.
- The process ignores the qualitative differences in the international dialing codes and focuses on the structural position of the digits within the phone number format.

In essence, the relationship showcases a methodical extraction of a specific part of the input data (phone numbers), highlighting how structured data can be parsed to retrieve specific information (in this case, the last three digits of the phone number)., and input as ['+106 769-858-438'] output is 438, input as ['+83 973-757-831'] output is 831, input as ['+62 647-787-775'] output is 775, input as ['+172 027-507-632'] output is 632, input as ['+72 001-050-856'] output is 856, input as ['+95 310-537-401'] output is 401, input as ['+6 775-969-238'] output is 238, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    """
    Extracts the last three digits from the given phone number string.
    
    Args:
    - phone_number (str): A string representing a phone number with an international dialing code prefix,
                          followed by a sequence of numbers separated by dashes.
    
    Returns:
    - str: The last three digits of the phone number.
    """
    # Split the phone number by dashes and take the last part
    last_part = phone_number.split('-')[-1]
    return last_part

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

# End time: 2024-04-09 12:47:58.898934
# Elapsed time in seconds: 12.837538346999963