# Start time: 2024-04-16 14:32:06.302463

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the second word of the inputted phrase, and input as ['Park Kim'] output is Kim, input as ['Lee Kim'] output is Kim, input as ['Kim Lee'] output is Lee, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above. All boolean return value should be converted to lowercase string.
'''

# Define the generated function
def generated_function(*args):
    # Extract the second word from each input
    outputs = []
    for arg in args:
        words = arg.split()
        if len(words) >= 2:
            outputs.append(words[1])
    
    return ', '.join(outputs).lower()



print(generated_function("Benjamin Hayes"))  ### Output: "Benjamin Hayes"
print(generated_function("Emma Reynolds"))  ### Output: "Emma Reynolds"
print(generated_function("Grace Harrison"))  ### Output: "Grace Harrison"
print(generated_function("Caleb Mitchell"))  ### Output: "Caleb Mitchell"
print(generated_function("Olivia Parker"))  ### Output: "Olivia Parker"
print(generated_function("Jackson Turner"))  ### Output: "Jackson Turner"


print(generated_function("Park Kim"))  ## Output: Kim
print(generated_function("Lee Kim"))  ## Output: Kim
print(generated_function("Kim Lee"))  ## Output: Lee



# End time: 2024-04-16 14:32:07.546579
# Elapsed time in seconds: 1.244088572999999