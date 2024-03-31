# Start time: 2024-03-30 19:56:10.529387

# Content: Given that given input as ['Susan Ann Chang'] output is Susan, given input as ['Ayako Tanaka'] output is Ayako, given input as ['Bobby T. smth'] output is Bobby, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def get_first_name(full_name):
    try:
        # Input: 'Susan Ann Chang'
        # Output: 'Susan'
        
        # Input: 'Ayako Tanaka'
        # Output: 'Ayako'
        
        # Input: 'Bobby T. smth'
        # Output: 'Bobby'
        
        first_name = full_name.split()[0]
        return first_name
    except Exception as e:
        print("Error: {}".format(e))

# Test cases
print(get_first_name('Susan Ann Chang'))
print(get_first_name('Ayako Tanaka'))
print(get_first_name('Bobby T. smth'))

# End time: 2024-03-30 19:56:12.512463
# Elapsed time in seconds: 1.9830421899996509