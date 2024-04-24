# Start time: 2024-04-10 14:48:25.594945

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
- The input column data consists of alphanumeric strings with various formats such as numbers, letters, and special characters.
- The input data includes words like CAP, BOX, PAX, and other identifiers that seem to categorize the information.
- There is a mix of uppercase and lowercase letters in the input data.
- The input data seems to contain product codes, identifiers, and possibly some descriptive information.

Summary for Output Column Data:
- The output column data consists of specific identifiers such as PAX, BOX, and other similar terms.
- The output data seems to be a subset of the input data, specifically focusing on certain identifiers or categories.
- The output data appears to be a selection or extraction from the input data based on specific criteria or patterns.

Relationship between Input and Output:
- The relationship between the input and output data seems to involve filtering or extracting specific information based on certain identifiers or keywords present in the input column data.
- The output data appears to be a subset of the input data, focusing on particular terms like PAX, BOX, etc.
- The output seems to be derived from the input by selecting or extracting relevant information based on predefined criteria or patterns present in the input data., and input as ['2283-332-44543 CAP DDT PPL445_ HEEN PAX 77820'] output is HEEN PAX 77820, input as ['44372-33-3223 TYYTE CAP BOX 1550 244 BOX PPSSA223_ PAX'] output is PAX, input as ['PRECISE 77 CLEAR BLUE 99WIE_ BOX 4403 PAX SSKA'] output is BOX 4403 PAX SSKA, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(*args):
    output_list = []
    for input_str in args:
        input_list = input_str.split()
        for i in range(len(input_list)):
            if input_list[i] == 'PAX' or input_list[i] == 'BOX':
                output_list.extend(input_list[i:])
                break
    return ' '.join(output_list)

# Test cases
print(generated_function('2283-332-44543 CAP DDT PPL445_ HEEN PAX 77820'))  # Output: HEEN PAX 77820
print(generated_function('44372-33-3223 TYYTE CAP BOX 1550 244 BOX PPSSA223_ PAX'))  # Output: PAX
print(generated_function('PRECISE 77 CLEAR BLUE 99WIE_ BOX 4403 PAX SSKA'))  # Output: BOX 4403 PAX SSKA
print(generated_function("2283-332-44543 CAP DDT PPL445_ HEEN PAX 77820"))  ## Output: HEEN PAX 77820
print(generated_function("44372-33-3223 TYYTE CAP BOX 1550 244 BOX PPSSA223_ PAX"))  ## Output: PAX
print(generated_function("PRECISE 77 CLEAR BLUE 99WIE_ BOX 4403 PAX SSKA"))  ## Output: BOX 4403 PAX SSKA

# End time: 2024-04-10 14:48:27.725172
# Elapsed time in seconds: 2.130170082999939


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

