# Start time: 2024-04-10 17:39:47.530532

'''
Prompt:
Given that input as ['80v', '3'] output is v, input as ['10hrs', '3'] output is hrs, input as ['7h', '2'] output is h, input as ['500m', '4'] output is m, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        num = int(input_str.split(',')[1])
        unit = input_str.split(',')[0][-1]
        return unit
    except:
        return "Invalid input format"

# Test cases
print(generated_function('80v,3'))
print(generated_function('10hrs,3'))
print(generated_function('7h,2'))
print(generated_function('500m,4'))
print(generated_function("80v", "3"))  ## Output: v
print(generated_function("10hrs", "3"))  ## Output: hrs
print(generated_function("7h", "2"))  ## Output: h
print(generated_function("500m", "4"))  ## Output: m

# End time: 2024-04-10 17:39:49.095025
# Elapsed time in seconds: 1.5644736109999258


# APPEND TEST SCRIPTS...
print(generated_function("80v", "3"))  ## Output: v
print(generated_function("10hrs", "3"))  ## Output: hrs
print(generated_function("7h", "2"))  ## Output: h
print(generated_function("500m", "4"))  ## Output: m


print(generated_function("80b", "3"))  ### Output: b
print(generated_function("500km", "4"))  ### Output: km
print(generated_function("10min", "3"))  ### Output: min
print(generated_function("7sec", "2"))  ### Output: sec
print(generated_function("12345km", "6"))  ### Output: km

# TEST SCRIPTS APPENDED!

