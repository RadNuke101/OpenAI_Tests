# Start time: 2024-04-09 19:44:35.257563

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: To generate summaries for the given data, we first need to understand the structure of the input and the corresponding output. The input data consists of strings that represent phone numbers in an international format, including a country code, a space, and then the phone number itself separated by dashes. The output data extracts the country code from each phone number, which is the sequence of digits immediately following the '+' sign and before the first space in the input.

### Summary for Input Column Data:
The input data is a collection of strings representing phone numbers in an international format. Each entry starts with a '+' sign followed by the country code, a space, and then the local phone number divided into segments by dashes. The country codes vary in length, ranging from one to three digits, indicating that the dataset includes phone numbers from various countries with different country code lengths. The local phone numbers are consistently formatted with three segments separated by dashes, although the number of digits in each segment can vary slightly. This format suggests a standardized approach to representing phone numbers but with variations to accommodate different national standards.

### Summary for Output Column Data:
The output data consists of integers representing the country codes extracted from the input phone numbers. These country codes range from one to three digits, reflecting the diversity of the international dialing codes assigned to different countries. The extraction process focuses solely on isolating the country code from the full phone number, disregarding the rest of the phone number. This output provides a simplified, numeric representation of the geographical origin (at the country level) of each phone number, which could be useful for analyses that require understanding or categorizing calls by country.

### Relationship Between Input and Output:
The relationship between the input and output data is a direct extraction process where the output is derived by isolating the country code from the input phone number. The input data provides a detailed, formatted representation of international phone numbers, while the output simplifies this information to just the country code. This transformation from a detailed string to a numeric country code highlights the focus on geographical categorization over individual phone number identification. The process underscores the importance of the country code in understanding the international aspect of the data, stripping away the specifics of the local phone number to concentrate on the broader geographical origin. This relationship is consistent across all data points, indicating a systematic approach to extracting key information (the country code) from a more complex dataset (the full phone number)., and input as ['+106 769-858-438'] output is 106, input as ['+83 973-757-831'] output is 83, input as ['+62 647-787-775'] output is 62, input as ['+172 027-507-632'] output is 172, input as ['+72 001-050-856'] output is 72, input as ['+95 310-537-401'] output is 95, input as ['+6 775-969-238'] output is 6, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    """
    Extracts the country code from a given phone number in international format.
    
    Args:
    phone_number (str): A string representing a phone number in international format.
    
    Returns:
    int: The country code extracted from the phone number.
    """
    # Find the position of the space to isolate the country code
    space_index = phone_number.find(' ')
    # Extract the country code, which is between the '+' sign and the first space
    country_code = phone_number[1:space_index]
    return int(country_code)

# Test cases
print(generated_function('+106 769-858-438'))  # Expected output: 106
print(generated_function('+83 973-757-831'))   # Expected output: 83
print(generated_function('+62 647-787-775'))   # Expected output: 62
print(generated_function('+172 027-507-632'))  # Expected output: 172
print(generated_function('+72 001-050-856'))   # Expected output: 72
print(generated_function('+95 310-537-401'))   # Expected output: 95
print(generated_function('+6 775-969-238'))    # Expected output: 6
print(generated_function("+106 769-858-438"))  ## Output: 106
print(generated_function("+83 973-757-831"))  ## Output: 83
print(generated_function("+62 647-787-775"))  ## Output: 62
print(generated_function("+172 027-507-632"))  ## Output: 172
print(generated_function("+72 001-050-856"))  ## Output: 72
print(generated_function("+95 310-537-401"))  ## Output: 95
print(generated_function("+6 775-969-238"))  ## Output: 6

# End time: 2024-04-09 19:44:44.066569
# Elapsed time in seconds: 8.80883962200096


# APPEND TEST SCRIPTS...
print(generated_function("+106 769-858-438"))  ## Output: 106
print(generated_function("+83 973-757-831"))  ## Output: 83
print(generated_function("+62 647-787-775"))  ## Output: 62
print(generated_function("+172 027-507-632"))  ## Output: 172
print(generated_function("+72 001-050-856"))  ## Output: 72
print(generated_function("+95 310-537-401"))  ## Output: 95
print(generated_function("+6 775-969-238"))  ## Output: 6


print(generated_function("+83 647-787-775"))  ### Output: 83
print(generated_function("+6 769-858-438"))  ### Output: 6
print(generated_function("+62 027-507-632"))  ### Output: 62
print(generated_function("+172 001-050-856"))  ### Output: 172
print(generated_function("+72 310-537-401"))  ### Output: 72
print(generated_function("+95 775-969-238"))  ### Output: 95
print(generated_function("+106 973-757-831"))  ### Output: 106

# TEST SCRIPTS APPENDED!

