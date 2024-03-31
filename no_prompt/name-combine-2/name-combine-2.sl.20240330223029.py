# Start time: 2024-03-30 22:43:41.999706

# Content: Given that given input as ['Nancy', 'FreeHafer'] output is Nancy F., given input as ['Andrew', 'Cencici'] output is Andrew C., given input as ['Jan', 'Kotas'] output is Jan K., given input as ['Mariya', 'Sergienko'] output is Mariya S., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def format_name(input_str):
    try:
        # Input: 'Nancy FreeHafer'
        # Output: 'Nancy F.'
        first_name, last_name = input_str.split()
        return f"{first_name} {last_name[0]}."
    except ValueError:
        print("Please provide both first name and last name separated by a space.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Test cases
print(format_name('Nancy FreeHafer'))  # Nancy F.
print(format_name('Andrew Cencici'))   # Andrew C.
print(format_name('Jan Kotas'))        # Jan K.
print(format_name('Mariya Sergienko')) # Mariya S.

# End time: 2024-03-30 22:43:43.955373
# Elapsed time in seconds: 1.9556133629994292