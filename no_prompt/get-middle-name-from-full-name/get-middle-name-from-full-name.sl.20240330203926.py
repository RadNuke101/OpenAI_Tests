# Start time: 2024-03-30 20:53:15.524815

# Content: Given that given input as ['susan ann chang'] output is ann, given input as ['ayako tanaka'] output is , given input as ['bobby t. smith'] output is t., given input as ['anthory r. tom brown'] output is r. tom, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_middle_name(name):
    try:
        # Input: 'susan ann chang'
        # Output: 'ann'
        parts = name.split()
        for part in parts:
            if len(part) == 1 and part.isalpha():
                return part + '.'
            elif len(part) > 1 and part.isalpha():
                return part
    except Exception as e:
        print("Error: ", e)

# Test cases
print(extract_middle_name('susan ann chang'))  # Output: ann
print(extract_middle_name('ayako tanaka'))  # Output: 
print(extract_middle_name('bobby t. smith'))  # Output: t.
print(extract_middle_name('anthory r. tom brown'))  # Output: r. tom

# End time: 2024-03-30 20:53:19.984686
# Elapsed time in seconds: 4.459753075001572