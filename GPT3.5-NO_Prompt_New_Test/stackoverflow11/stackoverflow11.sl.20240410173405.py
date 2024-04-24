# Start time: 2024-04-10 17:46:50.930468

'''
Prompt:
Given that input as ['2283-332-44543 CAP DDT PPL445_ HEEN PAX 77820'] output is HEEN PAX 77820, input as ['44372-33-3223 TYYTE CAP BOX 1550 244 BOX PPSSA223_ PAX'] output is PAX, input as ['PRECISE 77 CLEAR BLUE 99WIE_ BOX 4403 PAX SSKA'] output is BOX 4403 PAX SSKA, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        input_str = input_str.split()
        for i in range(len(input_str)):
            if input_str[i].isnumeric() and input_str[i+1].isalpha():
                return ' '.join(input_str[i-1:])
    except:
        return None

# Test cases
print(generated_function('2283-332-44543 CAP DDT PPL445_ HEEN PAX 77820'))  # Output: HEEN PAX 77820
print(generated_function('44372-33-3223 TYYTE CAP BOX 1550 244 BOX PPSSA223_ PAX'))  # Output: PAX
print(generated_function('PRECISE 77 CLEAR BLUE 99WIE_ BOX 4403 PAX SSKA'))  # Output: BOX 4403 PAX SSKA
print(generated_function("2283-332-44543 CAP DDT PPL445_ HEEN PAX 77820"))  ## Output: HEEN PAX 77820
print(generated_function("44372-33-3223 TYYTE CAP BOX 1550 244 BOX PPSSA223_ PAX"))  ## Output: PAX
print(generated_function("PRECISE 77 CLEAR BLUE 99WIE_ BOX 4403 PAX SSKA"))  ## Output: BOX 4403 PAX SSKA

# End time: 2024-04-10 17:46:52.930675
# Elapsed time in seconds: 2.0001467279998906


# APPEND TEST SCRIPTS...
print(generated_function("2283-332-44543 CAP DDT PPL445_ HEEN PAX 77820"))  ## Output: HEEN PAX 77820
print(generated_function("44372-33-3223 TYYTE CAP BOX 1550 244 BOX PPSSA223_ PAX"))  ## Output: PAX
print(generated_function("PRECISE 77 CLEAR BLUE 99WIE_ BOX 4403 PAX SSKA"))  ## Output: BOX 4403 PAX SSKA


print(generated_function("PPSSA223_ P"))  ### Output: P
print(generated_function("2283-332 PPL445_ PAX 77820 HEEN"))  ### Output: PAX 77820 HEEN
print(generated_function("PRECISE 99WIE_ BOX 4403 SSKA PAX"))  ### Output: BOX 4403 SSKA PAX
print(generated_function("PRECISE 77 BLUE CLEAR 99WIE_ BOX 4403 PAX SSKA AID AKLD IEKD OSID"))  ### Output: BOX 4403 PAX SSKA AID AKLD IEKD OSID
print(generated_function("44372-33-3223 TYYTE 1550 CAP BOX 244 BOX PPSSA223_ PAX"))  ### Output: PAX
print(generated_function("2283-332-44543 DDT CAP PPL445_ HEEN 77820 PAX"))  ### Output: HEEN 77820 PAX

# TEST SCRIPTS APPENDED!

