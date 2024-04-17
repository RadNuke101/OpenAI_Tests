# Start time: 2024-04-16 21:31:20.059299

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the number of non-zero consecutive numbers, and input as: "7 0 0 5 4 4" output is: 3, input as: "0 0 2 3 3 0" output is: 3, input as: "5 6 4 6 0 7" output is: 4, input as: "0 4 5 0 0 2" output is: 2, input as: "3 0 3 0 1 2" output is: 2, input as: "5 3 2 5 6 1" output is: 6, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above. All boolean return value should be converted to lowercase string.
'''

# Define the function to count the number of non-zero consecutive numbers
def generated_function(*args):
    results = []
    for arg in args:
        count = 0
        max_count = 0
        for num in arg.split():
            if int(num) != 0:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
        results.append(str(max_count))
    return results



print(generated_function("8 7 1 6 0 3"))  ### Output: "8 7 1 6 0 3"
print(generated_function("8 7 1 6 4 0"))  ### Output: "8 7 1 6 4 0"
print(generated_function("9 0 1 0 1 3"))  ### Output: "9 0 1 0 1 3"
print(generated_function("0 7 0 6 0 0"))  ### Output: "0 7 0 6 0 0"
print(generated_function("9 0 1 5 4 4"))  ### Output: "9 0 1 5 4 4"


print(generated_function("7 0 0 5 4 4"))  ## Output: 3
print(generated_function("0 0 2 3 3 0"))  ## Output: 3
print(generated_function("5 6 4 6 0 7"))  ## Output: 4
print(generated_function("0 4 5 0 0 2"))  ## Output: 2
print(generated_function("3 0 3 0 1 2"))  ## Output: 2
print(generated_function("5 3 2 5 6 1"))  ## Output: 6



# End time: 2024-04-16 21:31:21.610942
# Elapsed time in seconds: 1.5516109629999733