# Start time: 2024-04-10 17:57:41.990096

'''
Prompt:
Given that input as ['humpty dumpty'] output is 2, input as ['humpty dumpty sat on a wall,'] output is 6, input as ['couldnt put humpty together again.'] output is 5, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        words = input_str.split()
        return len(words)
    except AttributeError:
        return "Input must be a string"
    except Exception as e:
        return str(e)

# Test cases
print(generated_function('humpty dumpty'))  # Output: 2
print(generated_function('humpty dumpty sat on a wall,'))  # Output: 6
print(generated_function('couldnt put humpty together again.'))  # Output: 5
print(generated_function("humpty dumpty"))  ## Output: 2
print(generated_function("humpty dumpty sat on a wall,"))  ## Output: 6
print(generated_function("couldnt put humpty together again."))  ## Output: 5

# End time: 2024-04-10 17:57:43.720514
# Elapsed time in seconds: 1.7303757539998514


# APPEND TEST SCRIPTS...
print(generated_function("humpty dumpty"))  ## Output: 2
print(generated_function("humpty dumpty sat on a wall,"))  ## Output: 6
print(generated_function("couldnt put humpty together again."))  ## Output: 5


print(generated_function("dumpty sat on wall a humpty,"))  ### Output: 6
print(generated_function("dumpty humpty"))  ### Output: 2
print(generated_function("put again humpty together couldnt."))  ### Output: 5
print(generated_function("please count total words in a cell."))  ### Output: 7

# TEST SCRIPTS APPENDED!

