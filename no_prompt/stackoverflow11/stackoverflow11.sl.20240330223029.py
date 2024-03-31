# Start time: 2024-03-30 22:47:45.874642

# Content: Given that given input as ['2283-332-44543 CAP DDT PPL445_ HEEN PAX 77820'] output is HEEN PAX 77820, given input as ['44372-33-3223 TYYTE CAP BOX 1550 244 BOX PPSSA223_ PAX'] output is PAX, given input as ['PRECISE 77 CLEAR BLUE 99WIE_ BOX 4403 PAX SSKA'] output is BOX 4403 PAX SSKA, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_info(input_str):
    try:
        # Split the input string by spaces
        parts = input_str.split()
        
        # Look for the specific pattern in the parts list
        for i in range(len(parts)):
            if parts[i] == 'PAX':
                return ' '.join(parts[i:])
        
        # If the pattern is not found, return None
        return None
    
    except Exception as e:
        return str(e)

# Test cases
input1 = '2283-332-44543 CAP DDT PPL445_ HEEN PAX 77820'
input2 = '44372-33-3223 TYYTE CAP BOX 1550 244 BOX PPSSA223_ PAX'
input3 = 'PRECISE 77 CLEAR BLUE 99WIE_ BOX 4403 PAX SSKA'

output1 = extract_info(input1)
output2 = extract_info(input2)
output3 = extract_info(input3)

print(output1)
print(output2)
print(output3)

# End time: 2024-03-30 22:47:51.462622
# Elapsed time in seconds: 5.591700648999904