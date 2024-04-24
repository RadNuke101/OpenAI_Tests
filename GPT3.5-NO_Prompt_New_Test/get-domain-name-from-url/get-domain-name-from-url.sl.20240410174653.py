# Start time: 2024-04-10 17:52:39.125456

'''
Prompt:
Given that input as ['https=//abc.com/def'] output is https=//abc.com/, input as ['http=//www.abc.com/def/cef'] output is http=//www.abc.com, input as ['http=//chandoo.org/wp/def-def'] output is http=//chandoo.org/, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        input_str = input_str.replace('[', '').replace(']', '').replace("'", '')
        parts = input_str.split('=')
        url = parts[1].split('/')[0]
        return f"{parts[0]}={url}/"
    except Exception as e:
        return f"Error: {e}"

# Test cases
print(generated_function('https=//abc.com/def'))
print(generated_function('http=//www.abc.com/def/cef'))
print(generated_function('http=//chandoo.org/wp/def-def'))
print(generated_function("https=//abc.com/def"))  ## Output: https=//abc.com/
print(generated_function("http=//www.abc.com/def/cef"))  ## Output: http=//www.abc.com
print(generated_function("http=//chandoo.org/wp/def-def"))  ## Output: http=//chandoo.org/

# End time: 2024-04-10 17:52:41.022077
# Elapsed time in seconds: 1.896570820999841


# APPEND TEST SCRIPTS...
print(generated_function("https=//abc.com/def"))  ## Output: https=//abc.com/
print(generated_function("http=//www.abc.com/def/cef"))  ## Output: http=//www.abc.com
print(generated_function("http=//chandoo.org/wp/def-def"))  ## Output: http=//chandoo.org/


print(generated_function("https=//abc.com/home"))  ### Output: https=//abc.com/
print(generated_function("http=//www.abc.com/home/category"))  ### Output: http=//www.abc.com
print(generated_function("http=//chandoo.org/wp/home-home"))  ### Output: http=//chandoo.org/

# TEST SCRIPTS APPENDED!

