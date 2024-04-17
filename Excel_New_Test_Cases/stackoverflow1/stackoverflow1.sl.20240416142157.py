# Start time: 2024-04-16 14:23:39.268367

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: remove "Inc" and everything after from input, and input as ['Trucking Inc.'] output is Trucking, input as ['New Truck Inc'] output is New Truck, input as ['ABV Trucking Inc, LLC'] output is ABV Trucking, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above. All boolean return value should be converted to lowercase string.
'''

# Define the function to remove "Inc" and everything after from input
def generated_function(*args):
    result = []
    for arg in args:
        if "Inc" in arg:
            result.append(arg.split("Inc")[0].strip())
    return result



print(generated_function("New House Inc"))  ### Output: "New House Inc"
print(generated_function("Brand New House Inc"))  ### Output: "Brand New House Inc"
print(generated_function("Housing Inc."))  ### Output: "Housing Inc."
print(generated_function("ABV Housing Inc, LLC"))  ### Output: "ABV Housing Inc, LLC"


print(generated_function("Trucking Inc."))  ## Output: Trucking
print(generated_function("New Truck Inc"))  ## Output: New Truck
print(generated_function("ABV Trucking Inc, LLC"))  ## Output: ABV Trucking



# End time: 2024-04-16 14:23:40.271200
# Elapsed time in seconds: 1.0028071020000056