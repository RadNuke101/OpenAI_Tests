# Start time: 2024-03-30 22:27:18.440266

# Content: Given that given input as ['Launa', 'Withers'] output is L. Withers, given input as ['Lakenya', 'Edison'] output is L. Edison, given input as ['Brendan', 'Hage'] output is B. Hage, given input as ['Bradford', 'Lango'] output is B. Lango, given input as ['Rudolf', 'Akiyama'] output is R. Akiyama, given input as ['Lara', 'Constable'] output is L. Constable, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def format_name(name):
    try:
        first_name, last_name = name.split()
        return f"{first_name[0].upper()}. {last_name}"
    except ValueError:
        print("Input should contain first name and last name separated by a space.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Test cases
print(format_name('Launa Withers'))  # Output: L. Withers
print(format_name('Lakenya Edison'))  # Output: L. Edison
print(format_name('Brendan Hage'))  # Output: B. Hage
print(format_name('Bradford Lango'))  # Output: B. Lango
print(format_name('Rudolf Akiyama'))  # Output: R. Akiyama
print(format_name('Lara Constable'))  # Output: L. Constable

# End time: 2024-03-30 22:27:24.119095
# Elapsed time in seconds: 5.678669082999477