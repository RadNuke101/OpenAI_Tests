# Start time: 2024-04-10 17:44:07.692403

'''
Prompt:
Given that input as ['zx66448', 'z'] output is x66448, input as ['zx66448', 'x'] output is z66448, input as ['zx66448', '6'] output is zx448, input as ['zx66448', '4'] output is zx668, input as ['zx66448', '8'] output is zx6644, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str, char):
    try:
        index = input_str.index(char)
        output = input_str[:index] + input_str[index+1:]
        return output
    except ValueError:
        print("Character not found in input string")
    except Exception as e:
        print("An error occurred:", e)

# Test cases
print(generated_function('zx66448', 'z'))
print(generated_function('zx66448', 'x'))
print(generated_function('zx66448', '6'))
print(generated_function('zx66448', '4'))
print(generated_function('zx66448', '8'))
print(generated_function("zx66448", "z"))  ## Output: x66448
print(generated_function("zx66448", "x"))  ## Output: z66448
print(generated_function("zx66448", "6"))  ## Output: zx448
print(generated_function("zx66448", "4"))  ## Output: zx668
print(generated_function("zx66448", "8"))  ## Output: zx6644

# End time: 2024-04-10 17:44:10.267181
# Elapsed time in seconds: 2.574749089999841


# APPEND TEST SCRIPTS...
print(generated_function("zx66448", "z"))  ## Output: x66448
print(generated_function("zx66448", "x"))  ## Output: z66448
print(generated_function("zx66448", "6"))  ## Output: zx448
print(generated_function("zx66448", "4"))  ## Output: zx668
print(generated_function("zx66448", "8"))  ## Output: zx6644


print(generated_function("abcdefgh00123", "c"))  ### Output: abdefgh00123
print(generated_function("abcdefgh00123", "f"))  ### Output: abcdegh00123
print(generated_function("abcdefgh00123", "b"))  ### Output: acdefgh00123
print(generated_function("abcdefgh00123", "0"))  ### Output: abcdefgh123
print(generated_function("abcdefgh00123", "a"))  ### Output: bcdefgh00123

# TEST SCRIPTS APPENDED!

