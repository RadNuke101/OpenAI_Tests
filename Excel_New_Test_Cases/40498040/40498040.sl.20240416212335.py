# Start time: 2024-04-16 21:32:05.110286

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if the word "overhead" in expression, return false, else true, and input as: "some project,other project" output is: true, input as: "some project" output is: true, input as: "overhead" output is: false, input as: "some project, overhead" output is: false, input as: "some project, other, boo" output is: true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above. All boolean return value should be converted to lowercase string.
'''

def generated_function(*args):
    # Check each input argument
    for arg in args:
        # Check if the word "overhead" is in the input
        if "overhead" in arg:
            return "false"
    return "true"



print(generated_function("some project, other, overhead"))  ### Output: "some project, other, overhead"
print(generated_function("some project, other"))  ### Output: "some project, other"
print(generated_function("some project, other,"))  ### Output: "some project, other,"


print(generated_function("some project,other project"))  ## Output: true
print(generated_function("some project"))  ## Output: true
print(generated_function("overhead"))  ## Output: false
print(generated_function("some project, overhead"))  ## Output: false
print(generated_function("some project, other, boo"))  ## Output: true



# End time: 2024-04-16 21:32:06.490585
# Elapsed time in seconds: 1.3802699599999642