# Start time: 2024-04-10 17:51:47.285898

'''
Prompt:
Given that input as ['C0abc', 'def'] output is C0abc, input as ['aabc', 'def'] output is def, input as ['C0dd', 'qwe'] output is C0dd, input as ['dd', 'qwe'] output is qwe, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        input_list = eval(input_str)
        if input_list[0][0].isupper() and input_list[0][1:].isalpha():
            return input_list[0]
        elif input_list[1][0].isupper() and input_list[1][1:].isalpha():
            return input_list[1]
        else:
            raise ValueError("Invalid input")
    except (SyntaxError, ValueError, IndexError):
        return "Invalid input"

# Test cases
print(generated_function("['C0abc', 'def']"))
print(generated_function("['aabc', 'def']"))
print(generated_function("['C0dd', 'qwe']"))
print(generated_function("['dd', 'qwe']"))
print(generated_function("C0abc", "def"))  ## Output: C0abc
print(generated_function("aabc", "def"))  ## Output: def
print(generated_function("C0dd", "qwe"))  ## Output: C0dd
print(generated_function("dd", "qwe"))  ## Output: qwe

# End time: 2024-04-10 17:51:49.568662
# Elapsed time in seconds: 2.2827022439998927


# APPEND TEST SCRIPTS...
print(generated_function("C0abc", "def"))  ## Output: C0abc
print(generated_function("aabc", "def"))  ## Output: def
print(generated_function("C0dd", "qwe"))  ## Output: C0dd
print(generated_function("dd", "qwe"))  ## Output: qwe


print(generated_function("aabc", "q1owieurqowiperuqwopieruwoqpiur"))  ### Output: q1owieurqowiperuqwopieruwoqpiur
print(generated_function("C0qopweirup", "joqiwejr"))  ### Output: C0qopweirup
print(generated_function("C0pqowieqioweruqoiwpru", "d"))  ### Output: C0pqowieqioweruqoiwpru
print(generated_function("qopweirup", "joqiwejr"))  ### Output: joqiwejr
print(generated_function("pqowieqioweruqoiwpru", "d"))  ### Output: d

# TEST SCRIPTS APPENDED!

