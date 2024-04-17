# Start time: 2024-04-16 21:01:10.836246

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the first word of the inputted phrase, and input as: ['Nancy FreeHafer'] output is: Nancy, input as: ['Andrew Cencici'] output is: Andrew, input as: ['Jan Kotas'] output is: Jan, input as: ['Mariya Sergienko'] output is: Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above. All boolean return value should be converted to lowercase string.
'''

# Define the generated function
def generated_function(input_str):
    # Split the input string by space and return the first word
    return input_str.split()[0]

# Test cases
print(generated_function('Nancy FreeHafer')) # Output: Nancy
print(generated_function('Andrew Cencici')) # Output: Andrew
print(generated_function('Jan Kotas')) # Output: Jan
print(generated_function('Mariya Sergienko')) # Output: Mariya



print(generated_function("Jackson Turner"))  ### Output: "Jackson Turner"
print(generated_function("Caleb Mitchell"))  ### Output: "Caleb Mitchell"
print(generated_function("Benjamin Hayes"))  ### Output: "Benjamin Hayes"
print(generated_function("Grace Harrison"))  ### Output: "Grace Harrison"
print(generated_function("Mason Thompson"))  ### Output: "Mason Thompson"
print(generated_function("Lily Anderson"))  ### Output: "Lily Anderson"
print(generated_function("Wyatt Davis"))  ### Output: "Wyatt Davis"
print(generated_function("Olivia Parker"))  ### Output: "Olivia Parker"
print(generated_function("Emma Reynolds"))  ### Output: "Emma Reynolds"


print(generated_function("Nancy FreeHafer"))  ## Output: Nancy
print(generated_function("Andrew Cencici"))  ## Output: Andrew
print(generated_function("Jan Kotas"))  ## Output: Jan
print(generated_function("Mariya Sergienko"))  ## Output: Mariya



# End time: 2024-04-16 21:01:12.635002
# Elapsed time in seconds: 1.798720223000032