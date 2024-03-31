# Start time: 2024-03-30 22:10:45.074719

# Content: Given that given input as ['Launa', 'Withers'] output is Launa Withers, given input as ['Lakenya', 'Edison'] output is Lakenya Edison, given input as ['Brendan', 'Hage'] output is Brendan Hage, given input as ['Bradford', 'Lango'] output is Bradford Lango, given input as ['Rudolf', 'Akiyama'] output is Rudolf Akiyama, given input as ['Lara', 'Constable'] output is Lara Constable, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def format_names(input_str):
    try:
        first_name, last_name = input_str.split()
        return f"{first_name} {last_name}"
    except ValueError:
        print("Input format is incorrect. Please provide two names separated by a space.")

# Test cases
print(format_names('Launa Withers'))  # Output: Launa Withers
print(format_names('Lakenya Edison'))  # Output: Lakenya Edison
print(format_names('Brendan Hage'))  # Output: Brendan Hage
print(format_names('Bradford Lango'))  # Output: Bradford Lango
print(format_names('Rudolf Akiyama'))  # Output: Rudolf Akiyama
print(format_names('Lara Constable'))  # Output: Lara Constable

# End time: 2024-03-30 22:10:49.603808
# Elapsed time in seconds: 4.528970897999898