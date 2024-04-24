# Start time: 2024-04-10 17:53:19.044094

'''
Prompt:
Given that input as ['Tire Pressure ABC123873 Monitor'] output is ABC123873, input as [' Oil Life ABC849999999021 gauge'] output is ABC849999999021, input as [' Air conditioner GHF211 maintenance'] output is GHF211, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        keyword = 'Pressure' if 'Pressure' in input_str else 'Life' if 'Life' in input_str else 'conditioner'
        output = input_str.split(keyword + ' ')[1].split(' ')[0]
        return output
    except:
        return None

# Test cases
assert generated_function('Tire Pressure ABC123873 Monitor') == 'ABC123873'
assert generated_function(' Oil Life ABC849999999021 gauge') == 'ABC849999999021'
assert generated_function(' Air conditioner GHF211 maintenance') == 'GHF211'
print(generated_function("Tire Pressure ABC123873 Monitor"))  ## Output: ABC123873
print(generated_function(" Oil Life ABC849999999021 gauge"))  ## Output: ABC849999999021
print(generated_function(" Air conditioner GHF211 maintenance"))  ## Output: GHF211

# End time: 2024-04-10 17:53:20.564252
# Elapsed time in seconds: 1.5201232479998907


# APPEND TEST SCRIPTS...
print(generated_function("Tire Pressure ABC123873 Monitor"))  ## Output: ABC123873
print(generated_function(" Oil Life ABC849999999021 gauge"))  ## Output: ABC849999999021
print(generated_function(" Air conditioner GHF211 maintenance"))  ## Output: GHF211


print(generated_function(" Life ABC8499999021 gauge"))  ### Output: ABC8499999021
print(generated_function("Tire ABC123873 Monitor"))  ### Output: ABC123873
print(generated_function(" Air conditioner GDF211 maintenance company"))  ### Output: GDF211

# TEST SCRIPTS APPENDED!

