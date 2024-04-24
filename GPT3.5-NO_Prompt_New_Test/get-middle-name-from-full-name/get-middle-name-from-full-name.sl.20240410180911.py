# Start time: 2024-04-10 18:19:54.890085

'''
Prompt:
Given that input as ['susan ann chang'] output is ann, input as ['ayako tanaka'] output is , input as ['bobby t. smith'] output is t., input as ['anthory r. tom brown'] output is r. tom, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(name):
    try:
        parts = name.split()
        for part in parts:
            if len(part) == 1 and part.isalpha():
                return part + '.'
            elif len(part) > 1 and part.isalpha():
                return part
    except AttributeError:
        return ""
    except Exception as e:
        return ""

# Test cases
print(generated_function('susan ann chang'))
print(generated_function('ayako tanaka'))
print(generated_function('bobby t. smith'))
print(generated_function('anthory r. tom brown'))
print(generated_function("susan ann chang"))  ## Output: ann
print(generated_function("ayako tanaka"))  ## Output: 
print(generated_function("bobby t. smith"))  ## Output: t.
print(generated_function("anthory r. tom brown"))  ## Output: r. tom

# End time: 2024-04-10 18:19:56.819835
# Elapsed time in seconds: 1.9297061809998013


# APPEND TEST SCRIPTS...
print(generated_function("susan ann chang"))  ## Output: ann
print(generated_function("ayako tanaka"))  ## Output: 
print(generated_function("bobby t. smith"))  ## Output: t.
print(generated_function("anthory r. tom brown"))  ## Output: r. tom


print(generated_function("olivia parker"))  ### Output: 
print(generated_function("emma von reynolds"))  ### Output: von
print(generated_function("caleb mitchell"))  ### Output: 
print(generated_function("grace f. harrison"))  ### Output: f.
print(generated_function("mason ann thompson"))  ### Output: ann
print(generated_function("wyatt thomas davis"))  ### Output: thomas
print(generated_function("jackson ann turner"))  ### Output: ann
print(generated_function("benjamin t. hayes"))  ### Output: t.
print(generated_function("lily anderson"))  ### Output: 

# TEST SCRIPTS APPENDED!

