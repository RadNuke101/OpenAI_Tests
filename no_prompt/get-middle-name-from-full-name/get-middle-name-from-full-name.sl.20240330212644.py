# Start time: 2024-03-30 21:40:32.988935

# Content: Given that given input as ['susan ann chang'] output is ann, given input as ['ayako tanaka'] output is , given input as ['bobby t. smith'] output is t., given input as ['anthory r. tom brown'] output is r. tom, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_middle_name(full_name):
    try:
        # Input: 'susan ann chang'
        # Output: 'ann'
        parts = full_name.split()
        if len(parts) == 3:
            return parts[1]
        
        # Input: 'ayako tanaka'
        # Output: ''
        if len(parts) == 2:
            return ''
        
        # Input: 'bobby t. smith'
        # Output: 't.'
        if len(parts) == 3 and len(parts[1]) == 2 and parts[1][-1] == '.':
            return parts[1]
        
        # Input: 'anthory r. tom brown'
        # Output: 'r. tom'
        if len(parts) > 3 and len(parts[1]) == 2 and parts[1][-1] == '.':
            return ' '.join(parts[1:3])

    except Exception as e:
        print("Error:", e)
    
    return None

# Test cases
print(extract_middle_name('susan ann chang'))  # Output: ann
print(extract_middle_name('ayako tanaka'))     # Output: 
print(extract_middle_name('bobby t. smith'))    # Output: t.
print(extract_middle_name('anthory r. tom brown'))  # Output: r. tom

# End time: 2024-03-30 21:40:35.597434
# Elapsed time in seconds: 2.6084349470002053