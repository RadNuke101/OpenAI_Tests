# Start time: 2024-03-30 18:58:43.611976

# Content: Given that given input as ['Launa', 'Withers'] output is Withers, L., given input as ['Lakenya', 'Edison'] output is Edison, L., given input as ['Brendan', 'Hage'] output is Hage, B., given input as ['Bradford', 'Lango'] output is Lango, B., given input as ['Rudolf', 'Akiyama'] output is Akiyama, R., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def format_name(name):
    try:
        first_name, last_name = name.split()
        return f"{last_name}, {first_name[0]}."
    except ValueError:
        print("Input should contain both first and last name separated by a space.")
    except:
        print("An error occurred.")

# Test cases
print(format_name('Launa Withers'))  # Output: Withers, L.
print(format_name('Lakenya Edison'))  # Output: Edison, L.
print(format_name('Brendan Hage'))  # Output: Hage, B.
print(format_name('Bradford Lango'))  # Output: Lango, B.
print(format_name('Rudolf Akiyama'))  # Output: Akiyama, R.

# End time: 2024-03-30 18:58:46.763209
# Elapsed time in seconds: 3.151165034999849