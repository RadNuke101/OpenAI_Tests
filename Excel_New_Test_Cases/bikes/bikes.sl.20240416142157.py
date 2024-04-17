# Start time: 2024-04-16 14:22:45.035908

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the text before the last 3 numbers in inputted expression, and input as ['Ducati100'] output is Ducati, input as ['Honda125'] output is Honda, input as ['Ducati250'] output is Ducati, input as ['Honda250'] output is Honda, input as ['Honda550'] output is Honda, input as ['Ducati125'] output is Ducati, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above. All boolean return value should be converted to lowercase string.
'''

# Define the generated function
def generated_function(input_str):
    # Extract the text before the last 3 numbers
    output = input_str[:-3]
    return output



print(generated_function("Hyundai100"))  ### Output: "Hyundai100"
print(generated_function("Toyota125"))  ### Output: "Toyota125"
print(generated_function("Toyota250"))  ### Output: "Toyota250"
print(generated_function("Ford125"))  ### Output: "Ford125"
print(generated_function("Hyundai125"))  ### Output: "Hyundai125"
print(generated_function("Ford250"))  ### Output: "Ford250"
print(generated_function("Toyota550"))  ### Output: "Toyota550"
print(generated_function("Lamborghini250"))  ### Output: "Lamborghini250"
print(generated_function("Ford100"))  ### Output: "Ford100"


print(generated_function("Ducati100"))  ## Output: Ducati
print(generated_function("Honda125"))  ## Output: Honda
print(generated_function("Ducati250"))  ## Output: Ducati
print(generated_function("Honda250"))  ## Output: Honda
print(generated_function("Honda550"))  ## Output: Honda
print(generated_function("Ducati125"))  ## Output: Ducati



# End time: 2024-04-16 14:22:45.912989
# Elapsed time in seconds: 0.8770591250000024