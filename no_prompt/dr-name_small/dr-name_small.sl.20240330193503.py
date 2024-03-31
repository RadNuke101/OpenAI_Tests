# Start time: 2024-03-30 19:46:00.852385

# Content: Given that given input as ['Nancy FreeHafer'] output is Dr. Nancy, given input as ['Andrew Cencici'] output is Dr. Andrew, given input as ['Jan Kotas'] output is Dr. Jan, given input as ['Mariya Sergienko'] output is Dr. Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def format_name(input_str):
    try:
        name = input_str.split()
        title = "Dr."
        first_name = name[0]
        return f"{title} {first_name}"
    except IndexError:
        print("Invalid input format. Please provide a full name.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Test cases
# input: 'Nancy FreeHafer', output: 'Dr. Nancy'
print(format_name('Nancy FreeHafer'))

# input: 'Andrew Cencici', output: 'Dr. Andrew'
print(format_name('Andrew Cencici'))

# input: 'Jan Kotas', output: 'Dr. Jan'
print(format_name('Jan Kotas'))

# input: 'Mariya Sergienko', output: 'Dr. Mariya'
print(format_name('Mariya Sergienko'))

# End time: 2024-03-30 19:46:03.191604
# Elapsed time in seconds: 2.3391948290000073