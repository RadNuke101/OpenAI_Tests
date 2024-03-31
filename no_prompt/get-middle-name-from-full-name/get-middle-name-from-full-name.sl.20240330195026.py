# Start time: 2024-03-30 20:04:52.652672

# Content: Given that given input as ['susan ann chang'] output is ann, given input as ['ayako tanaka'] output is , given input as ['bobby t. smith'] output is t., given input as ['anthory r. tom brown'] output is r. tom, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_middle_name(full_name):
    try:
        # Input: 'susan ann chang'
        # Output: ann
        names = full_name.split()
        middle_name = ""
        for name in names:
            if len(name) == 1 and name.isalpha():
                middle_name += name + "."
            elif len(name) > 1 and name.isalpha():
                middle_name += name + " "
        return middle_name.strip()
    except Exception as e:
        print("Error: ", e)

# Test cases
print(extract_middle_name('susan ann chang'))  # Output: ann
print(extract_middle_name('ayako tanaka'))  # Output: 
print(extract_middle_name('bobby t. smith'))  # Output: t.
print(extract_middle_name('anthory r. tom brown'))  # Output: r. tom

# End time: 2024-03-30 20:04:54.500489
# Elapsed time in seconds: 1.8491075800002363