# Start time: 2024-03-30 22:30:24.234128

# Content: Given that given input as ['2283-332-44543 CAP DDT PPL445_ HEEN PAX 77820'] output is HEEN PAX 77820, given input as ['44372-33-3223 TYYTE CAP BOX 1550 244 BOX PPSSA223_ PAX'] output is PAX, given input as ['PRECISE 77 CLEAR BLUE 99WIE_ BOX 4403 PAX SSKA'] output is BOX 4403 PAX SSKA, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_info(input_str):
    try:
        # Input: '2283-332-44543 CAP DDT PPL445_ HEEN PAX 77820'
        # Output: 'HEEN PAX 77820'
        
        # Input: '44372-33-3223 TYYTE CAP BOX 1550 244 BOX PPSSA223_ PAX'
        # Output: 'PAX'
        
        # Input: 'PRECISE 77 CLEAR BLUE 99WIE_ BOX 4403 PAX SSKA'
        # Output: 'BOX 4403 PAX SSKA'
        
        parts = input_str.split()
        for i in range(len(parts)):
            if parts[i] == 'PAX':
                return ' '.join(parts[i:])
        
        return None
    except Exception as e:
        return None

# Test cases
print(extract_info('2283-332-44543 CAP DDT PPL445_ HEEN PAX 77820'))  # Output: HEEN PAX 77820
print(extract_info('44372-33-3223 TYYTE CAP BOX 1550 244 BOX PPSSA223_ PAX'))  # Output: PAX
print(extract_info('PRECISE 77 CLEAR BLUE 99WIE_ BOX 4403 PAX SSKA'))  # Output: BOX 4403 PAX SSKA

# End time: 2024-03-30 22:30:29.068012
# Elapsed time in seconds: 4.834978888000478