# Start time: 2024-03-30 23:50:46.146322

# Content: Given that given input as ['938-242-504'] output is 938.242.504, given input as ['308-916-545'] output is 308.916.545, given input as ['623-599-749'] output is 623.599.749, given input as ['981-424-843'] output is 981.424.843, given input as ['118-980-214'] output is 118.980.214, given input as ['244-655-094'] output is 244.655.094, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def format_phone_number(phone_number):
    try:
        # Convert input string to list of numbers
        phone_number_list = phone_number.split('-')
        
        # Format the phone number with periods
        formatted_phone_number = '.'.join(phone_number_list)
        
        return formatted_phone_number
    except Exception as e:
        return "Error: Invalid input"

# Test cases
print(format_phone_number('938-242-504'))  # Output should be 938.242.504
print(format_phone_number('308-916-545'))  # Output should be 308.916.545
print(format_phone_number('623-599-749'))  # Output should be 623.599.749
print(format_phone_number('981-424-843'))  # Output should be 981.424.843
print(format_phone_number('118-980-214'))  # Output should be 118.980.214
print(format_phone_number('244-655-094'))  # Output should be 244.655.094

# End time: 2024-03-30 23:50:51.375851
# Elapsed time in seconds: 5.229443336000259