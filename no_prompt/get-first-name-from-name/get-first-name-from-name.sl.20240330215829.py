# Start time: 2024-03-30 22:03:56.397599

# Content: Given that given input as ['Susan Ann Chang'] output is Susan, given input as ['Ayako Tanaka'] output is Ayako, given input as ['Bobby T. smth'] output is Bobby, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_first_name(full_name):
    try:
        # Input: 'Susan Ann Chang'
        # Output: 'Susan'
        
        # Input: 'Ayako Tanaka'
        # Output: 'Ayako'
        
        # Input: 'Bobby T. smth'
        # Output: 'Bobby'
        
        parts = full_name.split()
        return parts[0]
    except (IndexError, AttributeError):
        return "Invalid input"

# Test cases
print(extract_first_name('Susan Ann Chang'))  # Output: Susan
print(extract_first_name('Ayako Tanaka'))     # Output: Ayako
print(extract_first_name('Bobby T. smth'))    # Output: Bobby

# End time: 2024-03-30 22:03:58.792654
# Elapsed time in seconds: 2.3949883529985527