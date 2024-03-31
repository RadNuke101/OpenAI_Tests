# Start time: 2024-03-30 21:09:30.795325

# Content: Given that given input as ['susan ann chang'] output is ann, given input as ['ayako tanaka'] output is , given input as ['bobby t. smith'] output is t., given input as ['anthory r. tom brown'] output is r. tom, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_middle_name(name):
    try:
        # Input: 'susan ann chang'
        # Output: 'ann'
        
        # Input: 'ayako tanaka'
        # Output: ''
        
        # Input: 'bobby t. smith'
        # Output: 't.'
        
        # Input: 'anthony r. tom brown'
        # Output: 'r. tom'
        
        parts = name.split()
        
        if len(parts) < 3:
            return ''
        
        middle_name = ' '.join(parts[1:-1])
        
        return middle_name
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Test cases
print(extract_middle_name('susan ann chang'))
print(extract_middle_name('ayako tanaka'))
print(extract_middle_name('bobby t. smith'))
print(extract_middle_name('anthony r. tom brown'))

# End time: 2024-03-30 21:09:34.394147
# Elapsed time in seconds: 3.598738737999156