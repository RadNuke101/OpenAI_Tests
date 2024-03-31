# Start time: 2024-03-30 21:42:08.091651

# Content: Given that given input as ['2283-332-44543 CAP DDT PPL445_ HEEN PAX 77820'] output is HEEN PAX 77820, given input as ['44372-33-3223 TYYTE CAP BOX 1550 244 BOX PPSSA223_ PAX'] output is PAX, given input as ['PRECISE 77 CLEAR BLUE 99WIE_ BOX 4403 PAX SSKA'] output is BOX 4403 PAX SSKA, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_info(input_str):
    try:
        parts = input_str.split()
        for i in range(len(parts)):
            if parts[i] == 'PAX':
                return ' '.join(parts[i:])
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return None

# Test cases
input1 = '2283-332-44543 CAP DDT PPL445_ HEEN PAX 77820'
output1 = 'HEEN PAX 77820'
print(f"Input: {input1} | Output: {extract_info(input1)}")

input2 = '44372-33-3223 TYYTE CAP BOX 1550 244 BOX PPSSA223_ PAX'
output2 = 'PAX'
print(f"Input: {input2} | Output: {extract_info(input2)}")

input3 = 'PRECISE 77 CLEAR BLUE 99WIE_ BOX 4403 PAX SSKA'
output3 = 'BOX 4403 PAX SSKA'
print(f"Input: {input3} | Output: {extract_info(input3)}")

# End time: 2024-03-30 21:42:11.094514
# Elapsed time in seconds: 3.002775250000923