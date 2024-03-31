# Start time: 2024-03-30 20:06:34.203795

# Content: Given that given input as ['2283-332-44543 CAP DDT PPL445_ HEEN PAX 77820'] output is HEEN PAX 77820, given input as ['44372-33-3223 TYYTE CAP BOX 1550 244 BOX PPSSA223_ PAX'] output is PAX, given input as ['PRECISE 77 CLEAR BLUE 99WIE_ BOX 4403 PAX SSKA'] output is BOX 4403 PAX SSKA, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_info(input_str):
    try:
        parts = input_str.split()
        for i in range(len(parts)):
            if parts[i].isnumeric():
                return ' '.join(parts[i:])
    except Exception as e:
        return str(e)

# Test cases
# input: '2283-332-44543 CAP DDT PPL445_ HEEN PAX 77820'
# expected output: 'HEEN PAX 77820'
print(extract_info('2283-332-44543 CAP DDT PPL445_ HEEN PAX 77820'))

# input: '44372-33-3223 TYYTE CAP BOX 1550 244 BOX PPSSA223_ PAX'
# expected output: 'PAX'
print(extract_info('44372-33-3223 TYYTE CAP BOX 1550 244 BOX PPSSA223_ PAX'))

# input: 'PRECISE 77 CLEAR BLUE 99WIE_ BOX 4403 PAX SSKA'
# expected output: 'BOX 4403 PAX SSKA'
print(extract_info('PRECISE 77 CLEAR BLUE 99WIE_ BOX 4403 PAX SSKA'))

# End time: 2024-03-30 20:06:37.604818
# Elapsed time in seconds: 3.400986876999923