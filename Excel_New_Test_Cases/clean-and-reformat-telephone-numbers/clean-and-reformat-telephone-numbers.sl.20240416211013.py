# Start time: 2024-04-16 21:11:06.410459

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: delete all "-", "<", ">", ".", and any spaces, and input as: "801-456-8765" output is: 8014568765, input as: "<978> 654-0299" output is: 9786540299, input as: "978.654.0299" output is: 9786540299, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above. All boolean return value should be converted to lowercase string.
'''

def generated_function(*args):
    result = []
    for arg in args:
        output = arg.replace("-", "").replace("<", "").replace(">", "").replace(".", "").replace(" ", "")
        result.append(output)
    return result



print(generated_function("801.456-8765"))  ### Output: "801.456-8765"
print(generated_function("(978) 654-0299"))  ### Output: "(978) 654-0299"
print(generated_function("978 654 0299"))  ### Output: "978 654 0299"


print(generated_function("801-456-8765"))  ## Output: 8014568765
print(generated_function("<978> 654-0299"))  ## Output: 9786540299
print(generated_function("978.654.0299"))  ## Output: 9786540299



# End time: 2024-04-16 21:11:07.301254
# Elapsed time in seconds: 0.8907756440000014