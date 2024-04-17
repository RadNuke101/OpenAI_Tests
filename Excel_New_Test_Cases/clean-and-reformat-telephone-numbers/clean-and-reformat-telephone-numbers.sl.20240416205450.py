# Start time: 2024-04-16 20:56:50.094877

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: delete all "-", "<", ">", ".", and any spaces, and input as: ['801-456-8765'] output is: 8014568765, input as: ['<978> 654-0299'] output is: 9786540299, input as: ['978.654.0299'] output is: 9786540299, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above. All boolean return value should be converted to lowercase string.
'''

# Define the function to remove specified characters from the input strings
def generated_function(*args):
    result = []
    for arg in args:
        result.append(arg.replace("-", "").replace("<", "").replace(">", "").replace(".", "").replace(" ", ""))
    return result



print(generated_function("801.456-8765"))  ### Output: "801.456-8765"
print(generated_function("(978) 654-0299"))  ### Output: "(978) 654-0299"
print(generated_function("978 654 0299"))  ### Output: "978 654 0299"


print(generated_function("801-456-8765"))  ## Output: 8014568765
print(generated_function("<978> 654-0299"))  ## Output: 9786540299
print(generated_function("978.654.0299"))  ## Output: 9786540299



# End time: 2024-04-16 20:56:51.129076
# Elapsed time in seconds: 1.0342212539999878